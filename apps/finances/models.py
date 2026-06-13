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

import uuid
from django.conf import settings
from django.db import models
from django_extensions.db.fields import AutoSlugField
from tree_queries.models import OrderableTreeNode
from core.models import TimeStampedModel, TimeStampedUUIDModel
from apps.finances.constants import FinancesAccountTypes

USER_MODEL = settings.AUTH_USER_MODEL


class Account(TimeStampedUUIDModel):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, related_name="accounts")
    nickname = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50, choices=FinancesAccountTypes)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, related_name="accounts")
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    bank = models.ForeignKey("Bank", on_delete=models.CASCADE, related_name="accounts", blank=True, null=True)
    account_number = models.CharField(max_length=4, unique=True, blank=True)

    # Default manager
    objects = models.Manager()

    class Meta:
        ordering = ["nickname"]
        verbose_name_plural = "Accounts"

    def __str__(self):
        bank_alias = self.bank.alias
        account_type = self.type.capitalize()
        account_number = self.account_number

        return f"{bank_alias} {account_type} account - {account_number}"


class Currency(TimeStampedModel):
    iso_code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    # Default manager
    objects = models.Manager()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f"({self.iso_code}) {self.symbol} {self.name}"


class Bank(TimeStampedUUIDModel):
    legal_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    bic = models.CharField(max_length=11)
    slug = AutoSlugField(populate_from="alias")

    # Default manager
    objects = models.Manager()

    class Meta:
        ordering = ["legal_name"]
        verbose_name_plural = "Banks"

    def __str__(self):
        return f"{self.legal_name}: {self.alias}"


class Category(OrderableTreeNode):
    name = models.CharField(max_length=100)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid7, editable=False, db_index=True)

    # Default manager
    objects = models.Manager()

    class Meta(OrderableTreeNode.Meta):
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"
