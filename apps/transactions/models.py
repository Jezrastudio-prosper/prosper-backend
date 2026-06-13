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


class Transaction(TimeStampedUUIDModel):
    account = models.ForeignKey("Account", on_delete=models.CASCADE, related_name="transactions")
    merchant = models.ForeignKey("Merchant", on_delete=models.CASCADE, related_name="transactions")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField()  # fixme
    status = models.CharField()  # fixme
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # Default manager
    objects = models.Manager()

    class Meta:
        ordering = [""]
        verbose_name_plural = ""

    def __str__(self):
        return f"{}"


class TransactionItem(models.Model):
    transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE, related_name="items")
    merchant_item = models.ForeignKey("MerchantItem", on_delete=models.CASCADE, related_name="items")
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()

    # Default manager
    objects = models.Manager()

    class Meta:
        ordering = [""]
        verbose_name_plural = ""

    def __str__(self):
        return f"{}"
