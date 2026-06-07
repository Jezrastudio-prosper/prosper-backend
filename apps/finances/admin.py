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

from .models import Account, Currency, Bank


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'updated_at',
        'uuid',
        'user',
        'nickname',
        'type',
        'currency',
        'current_balance',
        'available_balance',
        'is_active',
        'bank',
        'account_number',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'user',
        'currency',
        'is_active',
        'bank',
    )
    date_hierarchy = 'created_at'
    list_select_related = ('bank', 'user')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'iso_code',
        'symbol',
        'name',
        'is_active',
    )
    list_filter = ('created_at', 'updated_at', 'is_active')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'legal_name',
        'alias',
        'bic',
        'slug',
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('slug',)
    date_hierarchy = 'created_at'
   