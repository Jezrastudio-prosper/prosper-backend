"""
Registers models with the Django admin site.

Docs: https://docs.djangoproject.com/en/stable/ref/contrib/admin/

Rules:
    - Register every model that needs to be managed via the admin interface.
    - Use ModelAdmin subclasses to customise list views, search, and filters.
    - Never put business logic here — admin actions should call services.

Example:
    @admin.register(Post)
    class PostAdmin(admin.ModelAdmin):
        list_display = ["title", "author", "is_published", "created_at"]
        list_filter = ["is_published"]
        search_fields = ["title", "author__username"]
"""
from django.contrib import admin

from .models import Transaction, TransactionItem


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'updated_at',
        'uuid',
        'account',
        'merchant',
        'category',
        'amount',
        'type',
        'status',
        'note',
        'date',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'account',
        'merchant',
        'category',
        'date',
    )
    date_hierarchy = 'created_at'


@admin.register(TransactionItem)
class TransactionItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'transaction',
        'merchant_item',
        'description',
        'quantity',
        'unit_price',
        'subtotal',
        'note',
    )
    list_filter = ('transaction', 'merchant_item')
