"""
Django ORM model definitions for this app.

Docs: https://docs.djangoproject.com/en/stable/topics/db/models/

Rules:
    - Models are pure data definitions — field declarations, Meta, and __str__ only.
    - Attach custom managers from managers.py for reusable queryset building blocks.
    - No business logic in models — that belongs in services.
    - No query composition in models — that belongs in selectors.
    - Use explicit field names and avoid relying on Django defaults for null/blank.

Example:
    class Post(models.Model):
        title = models.CharField(max_length=200)
        body = models.TextField()
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
        status = models.CharField(max_length=20, choices=PostStatus.choices, default=PostStatus.DRAFT)
        created_at = models.DateTimeField(auto_now_add=True)

        objects = models.Manager()
        published = PublishedManager()

        class Meta:
            ordering = ["-created_at"]

        def __str__(self):
            return self.title
"""
from django.db import models
from core.models import TimeStampedModel, TimeStampedUUIDModel
from apps.transactions.constants import TransactionType, TransactionStatus


class Transaction(TimeStampedUUIDModel):
    account = models.ForeignKey("finances.Account", on_delete=models.CASCADE, related_name="transactions")
    merchant = models.ForeignKey("merchants.Merchant", on_delete=models.CASCADE, related_name="transactions")
    category = models.ForeignKey("finances.Category", on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100, choices=TransactionType)
    status = models.CharField(max_length=100, choices=TransactionStatus)
    note = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # Default manager
    objects = models.Manager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Transactions"

    def __str__(self):
        currency_symbol = self.account.currency.symbol
        return f"{self.category.name.capitalize()} of {currency_symbol}{self.amount} on {self.date or 'unpaid'}"


class TransactionItem(models.Model):
    transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE, related_name="transaction_items")
    merchant_item = models.ForeignKey("merchants.MerchantItem", on_delete=models.CASCADE, related_name="transaction_items")
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True)

    # Default manager
    objects = models.Manager()

    class Meta:
        ordering = ["transaction"]
        verbose_name_plural = "Transaction Items"

    def __str__(self):
        return f"{self.merchant_item} x{self.quantity} — {self.subtotal}"
