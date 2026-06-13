"""
DRF pagination classes controlling how list responses are split into pages.

Docs: https://www.django-rest-framework.org/api-guide/pagination/

Rules:
    - Use PageNumberPagination for stable, small datasets where users navigate by page.
    - Use CursorPagination for large or frequently-updated datasets to avoid page drift.
    - Always set a max_page_size to prevent unbounded queries.
    - Apply via pagination_class on the view or set DEFAULT_PAGINATION_CLASS in settings.

Example:
    class StandardPageNumberPagination(PageNumberPagination):
        page_size = 20
        page_size_query_param = "page_size"
        max_page_size = 100
"""
