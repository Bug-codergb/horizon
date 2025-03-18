from rest_framework.response import Response
from rest_framework.views import APIView
from apps.role.models import Role,UserRole
from utils.response import RetResponse
from rest_framework.generics import ListAPIView,DestroyAPIView
from apps.role.serializers.role import RoleSerializer
from utils.pagination import CustomPageNumberPagination

class CreateRoleView(APIView):
  def post(self,request):
    role_name = request.data.get("name")
    Role.objects.create(name=role_name)
    return RetResponse.success(None,None)

class UserRoleView(APIView):
  def post(self,request):
    user_id = request.data.get("user_id")
    role_list = request.data.get("role_list")
    UserRole.objects.filter(user_id_id = user_id).delete()
    l = []
    for index,role_id in enumerate(role_list):
     l.append(UserRole(user_id_id=user_id,role_id_id = role_id))
    UserRole.objects.bulk_create(l)
    return RetResponse.success(None,None)

class AllRoleView(ListAPIView):
  queryset = Role.objects.all().order_by('-createTime')
  serializer_class = RoleSerializer
  pagination_class = CustomPageNumberPagination

class DeleteRoleView(DestroyAPIView):
  queryset = Role.objects.all()
  serializer_class = RoleSerializer
  lookup_field = 'id'