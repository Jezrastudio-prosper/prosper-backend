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
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.transactions.models import Transaction, TransactionItem
from apps.merchants.serializers.output import MerchantItemOutputSerializer


class TransactionItemOutputSerializer(ModelSerializer):
    merchant_item = MerchantItemOutputSerializer()
    class Meta:
        model = TransactionItem
        fields = [
            "merchant_item",
            "description",
            "quantity",
            "unit_price",
            "subtotal",
            "note"
        ]


class TransactionOutputSerializer(ModelSerializer):
    transaction_items = TransactionItemOutputSerializer(many=True)

    class Meta:
        model = Transaction
        fields = [
            "uuid",
            "created_at",
            "updated_at",
            "date",
            "account",  # fk
            "merchant",  # fk
            "category",
            "amount",
            "type",
            "status",
            "note",
            "transaction_items"
        ]
