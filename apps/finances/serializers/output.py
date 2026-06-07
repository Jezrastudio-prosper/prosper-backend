"""
Output serializers responsible for shaping data returned in API responses.

Docs: https://www.django-rest-framework.org/api-guide/serializers/

Rules:
    - Inherit from ModelSerializer with explicit fields — avoid fields = "__all__".
    - No validation logic — output serializers are for representation only.
    - Use SerializerMethodField for computed or transformed values.
    - Use source= to remap field names without changing the model.
    - These can and should be reused across any endpoint returning the same resource.

Example:
    class PostOutputSerializer(serializers.ModelSerializer):
        author_name = serializers.CharField(source="author.get_full_name")
        tag_list = serializers.SerializerMethodField()

        class Meta:
            model = Post
            fields = ["id", "title", "body", "author_name", "tag_list", "created_at"]

        def get_tag_list(self, obj):
            return [tag.name for tag in obj.tags.all()]
"""
