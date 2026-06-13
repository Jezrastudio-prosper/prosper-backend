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

from core.models import TimeStampedUUIDModel


class Merchant(TimeStampedUUIDModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # Default manager
    objects = models.Manager()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Merchants"

    def __str__(self):
        return f"{self.name}"


class MerchantItem(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE, related_name="merchant_items")
    merchant = models.ForeignKey("Merchant", on_delete=models.CASCADE, related_name="merchant_items")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Default manager
    objects = models.Manager()

    class Meta:
        ordering = ["item__name"]
        verbose_name_plural = "Merchant Items"

    def __str__(self):
        return f"{self.item.name}"
