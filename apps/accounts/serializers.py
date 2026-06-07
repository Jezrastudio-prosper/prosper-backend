from rest_framework.serializers import ModelSerializer
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


class UserSerializer(ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ["username"]
