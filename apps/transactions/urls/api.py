"""
URL routing for DRF API endpoints.

Docs: https://www.django-rest-framework.org/api-guide/routers/

Rules:
    - Mount these under /api/v1/ in the root urls.py using include().
    - Use an app_name for namespacing so reverse() calls are unambiguous.
    - Keep URL patterns shallow and RESTful — avoid deeply nested resource paths.
    - For ViewSets, prefer explicit path() declarations over DefaultRouter unless the
      app has many standard CRUD endpoints.

Example:
    # root urls.py
    path("api/v1/", include(("posts.urls.api", "posts_api"), namespace="posts_api")),

    # this file
    urlpatterns = [
        path("posts/", PostListCreateView.as_view(), name="post-list-create"),
        path("posts/<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    ]
"""
from apps.transactions.views import api as views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"transactions", views.TransactionViewSet, basename="transactions")
urlpatterns = [

]

urlpatterns += router.urls
