from rest_framework.generics import ListAPIView, DestroyAPIView
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.menu.models import Menu,RoleMenu
from apps.role.models import Role
from utils.response import RetResponse
from apps.menu.serializers.menu import MenuSerializer,RoleMenuSerializer,SimpleRoleMenuSerializer
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
  serializer_class = MenuSerializer
  pagination_class = CustomPageNumberPagination
  def get_queryset(self):
    print(self.request.user_name)
    queryset = Menu.objects.filter(parent__isnull=True).order_by('sort')
    return queryset

class SetRoleMenuView(APIView):
  def post(self,request):
    data_object = request.data
    role_id = data_object['role_id']
    menu_list = data_object['menu_list']

    RoleMenu.objects.filter(role_id = role_id).delete()
    l=[]
    for index,menu in enumerate(menu_list):
      print(menu)
      l.append(RoleMenu(menu_id=menu['menu_id'],role_id=role_id,half=menu['half']))
    RoleMenu.objects.bulk_create(l)
    return RetResponse.success(None,None)

class DeleteMenu(DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class UserRoleMenuListView(APIView):
  def get(self,request,id):
    with connection.cursor() as cursor:
        cursor.execute("""
          select *
            from menu as m
            where parent_id is  null and m.id in (
              select distinct(m.id) as id
            from user as u
            left join user_role ur on u.user_id = ur.user_id
            left join role_menu rm on ur.role_id = rm.role_id
            LEFT JOIN menu as m on m.id = rm.menu_id
            LEFT JOIN role on role.id = rm.role_id
            where u.user_id = %s
            )
          order by sort asc  
        """, [id])
        rows = cursor.fetchall()

    if rows:
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        ser = RoleMenuSerializer(instance=data,many=True,context={'user_id':id})
        return RetResponse.success(ser.data, None)
    else :
      return RetResponse.success(None, None)

class RoleMenuView(APIView):
  def get(self,request,id):
    role_menu = RoleMenu.objects.filter(role_id=id)
    ser = SimpleRoleMenuSerializer(instance=role_menu,many=True)
    return RetResponse.success(ser.data,None)