from rest_framework.serializers import ModelSerializer
from apps.role.models import Role
from apps.user.serializers.user import UserSerializer
class RoleSerializer(ModelSerializer):
  users = UserSerializer(many=True)
  class Meta:
    model=Role
    fields="__all__"