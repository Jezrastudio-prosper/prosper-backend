"""
Input serializers responsible for validating incoming request data.

Docs: https://www.django-rest-framework.org/api-guide/serializers/

Rules:
    - Use validate_<field>() for field-level validation and validate() for cross-field validation.
    - Accept user via __init__ kwargs when a field's queryset depends on who is making the request.
    - Pass validated_data directly to a service — the serializer's job ends there.

Example:
    class PostCreateInputSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=200)
        body = serializers.CharField()

        def validate_title(self, value):
            if Post.objects.filter(title=value).exists():
                raise serializers.ValidationError("A post with this title already exists.")
            return value
"""
from rest_framework.serializers import ModelSerializer, ValidationError

from apps.finances.models import Account, Category
from apps.accounts.serializers import UserSerializer


class AccountInputSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Account
        fields = [
            "user",
            "nickname",
            "type",
            "currency",
            "current_balance",
            "available_balance",
            "bank",
            "account_number",
        ]


class CategoryInputSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "uuid",
            "name",
            "parent"
        ]

    def validate(self, attrs):
        parent = attrs.get('parent')
        # Prevent a category from becoming its own parent during updates
        if self.instance and parent == self.instance:
            raise ValidationError({"parent": "A category cannot be its own parent."})
        # Prevent loop: moving a parent into one of its own subcategories
        if self.instance and parent and parent in self.instance.descendants():
            raise ValidationError({"parent": "A category cannot be a child of its own sub-category."})
        return attrs
