"""
Output serializers responsible for shaping data returned in API responses.

Docs: https://www.django-rest-framework.org/api-guide/serializers/

Rules:
    - Inherit from ModelSerializer with explicit fields — avoid fields = "__all__".
    - No validation logic — output serializers are for representation only.
    - Use SerializerMethodField for computed or transformed values.
    - Use source= to remap field names without changing the model.
    - These can and should be reused across any endpoint returning the same resource.

Example:
    class PostOutputSerializer(serializers.ModelSerializer):
        author_name = serializers.CharField(source="author.get_full_name")
        tag_list = serializers.SerializerMethodField()

        class Meta:
            model = Post
            fields = ["id", "title", "body", "author_name", "tag_list", "created_at"]

        def get_tag_list(self, obj):
            return [tag.name for tag in obj.tags.all()]
"""

from rest_framework.serializers import ModelSerializer, ReadOnlyField

from apps.finances.models import Account, Bank, Currency, Category
from apps.accounts.serializers import UserSerializer


class AccountOutputSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Account
        fields = [
            "uuid",
            "user",
            "nickname",
            "type",
            "currency",
            "current_balance",
            "available_balance",
            "bank",
            "account_number",
        ]


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            "iso_code",
            "symbol",
            "name",
        ]


class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            "legal_name",
            "alias",
            "bic",
            "slug",
        ]


class CategoryOutputSerializer(ModelSerializer):
    parent_name = ReadOnlyField(source='parent.name')

    class Meta:
        model = Category
        fields = [
            "uuid",
            "name",
            "parent",
            "parent_name",
        ]
