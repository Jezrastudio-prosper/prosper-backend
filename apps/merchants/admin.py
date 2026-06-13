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

from .models import Merchant, MerchantItem


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'updated_at',
        'uuid',
        'name',
        'description',
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(MerchantItem)
class MerchantItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'merchant', 'price')
    list_filter = ('item', 'merchant')
