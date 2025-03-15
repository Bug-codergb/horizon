from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.menu.models import Menu,RoleMenu
from utils.response import RetResponse
from apps.menu.serializers.menu import MenuSerializer
from utils.pagination import CustomPageNumberPagination
#创建菜单
class CreateMenuView(APIView):
  def post(self,request):
    menu_obj = request.data
    Menu.objects.create(name=menu_obj['name'],
                        path = menu_obj['path'],
                        component=menu_obj['component'],
                        meta = menu_obj['meta'],
                        sort=menu_obj['sort'],
                        parent_id=menu_obj['parent_id'])
    return RetResponse.success(None,None)
# 所有菜单
class AllMenuView(ListAPIView):
  queryset = Menu.objects.filter(parent__isnull=True).order_by('sort')
  serializer_class = MenuSerializer
  pagination_class = CustomPageNumberPagination

class SetRoleMenuView(APIView):
  def post(self,request):
    data_object = request.data

    RoleMenu.objects.create(menu_id=data_object['menu_id'],
                            role_id=data_object['role_id'],
                            half=data_object['half'])
    return RetResponse.success(None,None)

class DeleteMenu(DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer