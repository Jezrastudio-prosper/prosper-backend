"""
DRF API views coordinating request handling for JSON endpoints.

Docs: https://www.django-rest-framework.org/api-guide/views/

Rules:
    - Views are thin coordinators — no business logic, no raw ORM queries.
    - Call selectors for reads, services for writes.
    - Catch domain exceptions from exceptions.py and map them to DRF Response status codes.
    - Never pass request objects into services or selectors.
    - Use input serializers for validation, output serializers for response shaping.
    - Always call check_object_permissions() after get_object() for object-level checks.

Example:
    class PostListCreateView(generics.GenericAPIView):
        permission_classes = [IsAuthenticated]

        def post(self, request):
            serializer = PostCreateInputSerializer(data=request.data, user=request.user)
            serializer.is_valid(raise_exception=True)
            try:
                post = create_post(user=request.user, **serializer.validated_data)
            except ValidationError as e:
                return Response({"detail": str(e)}, status=400)
            return Response(PostOutputSerializer(post).data, status=201)
"""

from rest_framework.viewsets import ModelViewSet
from core.mixins import MultiSerializerMixin
from apps.transactions.models import Transaction
from apps.transactions.serializers import output as output_serializers
from apps.transactions.serializers import input as input_serializers


class TransactionViewSet(MultiSerializerMixin, ModelViewSet):
    queryset = Transaction.objects.all()
    input_serializer_class = input_serializers.TransactionInputSerializer
    output_serializer_class = output_serializers.TransactionOutputSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
