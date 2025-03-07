from rest_framework.serializers import ModelSerializer,SerializerMethodField
from apps.user.models import User
#from apps.role.serializers.role import RoleSerializer
class UserSerializer(ModelSerializer):
  roles = SerializerMethodField() #RoleSerializer(many=True)
  class Meta:
    model=User
    fields="__all__"
  def get_roles(self,obj):
    roles = obj.role_set.all()#role_set是反向查询时，默认的名称
    return [{'id': role.id, 'name': role.name} for role in roles]