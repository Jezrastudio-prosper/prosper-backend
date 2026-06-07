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
from rest_framework.serializers import ModelSerializer

from apps.finances.models import Account
from apps.accounts.serializers import UserSerializer


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account

        class AccountSerializer(ModelSerializer):
            user = UserSerializer(read_only=True)

            class Meta:
                model = Account
                fields = [
                    "nickname",
                    "type",
                    "currency",
                    "current_balance",
                    "available_balance",
                    "bank",
                    "account_number",
                ]
