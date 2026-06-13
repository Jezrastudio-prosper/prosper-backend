"""
End-to-end tests for DRF API views in views/api.py.

Docs: https://www.django-rest-framework.org/api-guide/testing/

Rules:
    - Use DRF's APIClient — not Django's plain test Client.
    - Test status codes, response shape, and permission boundaries.
    - Do not re-test selector or service logic here — assume those layers are correct.
    - Test both authenticated and unauthenticated requests for protected endpoints.
    - Use force_authenticate() over credentials to keep tests fast.

Example:
    @pytest.mark.django_db
    def test_post_create_returns_201(authenticated_client):
        client, user = authenticated_client
        response = client.post(reverse("posts_api:post-list-create"), {"title": "Hi", "body": "."})
        assert response.status_code == 201
        assert response.data["title"] == "Hi"

    @pytest.mark.django_db
    def test_post_create_requires_authentication(api_client):
        response = api_client.post(reverse("posts_api:post-list-create"), {})
        assert response.status_code == 401
"""
