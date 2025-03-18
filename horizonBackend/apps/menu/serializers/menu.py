from rest_framework.serializers import ModelSerializer,SerializerMethodField
from django.db import connection
from apps.menu.models import Menu,RoleMenu
import json
#单个菜单
class RawMenuSerializer(ModelSerializer):
  meta = SerializerMethodField()
  children = SerializerMethodField()
  class Meta:
    model = Menu
    fields = ["id", "name", "path", "component", "meta", "createTime", "parent_id", "children", "sort"]
  def get_children(self, obj):
    # 递归获取子菜单
    return []
  def get_meta(self, obj):
    ret = json.loads(obj.meta) if obj.meta != None else None
    return ret

#所有菜单序列化
class MenuSerializer(ModelSerializer):
  children = SerializerMethodField()
  meta = SerializerMethodField()
  class Meta:
    model = Menu
    fields = ["id","name","path","component","meta","createTime","parent_id","children","sort"]
  def get_children(self, obj):
    # 递归获取子菜单
    children = obj.children.all().order_by('sort')
    return MenuSerializer(children, many=True).data
  def get_meta(self,obj):
    ret = json.loads(obj.meta) if obj.meta != None else None
    return ret
#角色菜单序列化
class RoleMenuSerializer(ModelSerializer):
  meta = SerializerMethodField()
  children = SerializerMethodField()
  class Meta:
    model = Menu
    fields = ["id", "name", "path", "component", "meta", "createTime","children", "parent_id", "sort"]

  def get_children(self, obj):
      # 递归获取子菜单
      user_id = self.context.get("user_id")
      with connection.cursor() as cursor:
        cursor.execute("""
            select *
              from menu
              where parent_id=%s and id in (
                select DISTINCT(m.id) as id
              from user as u
              left join user_role ur on u.user_id = ur.user_id
              left join role_menu rm on ur.role_id = rm.role_id
              LEFT JOIN menu as m on m.id = rm.menu_id
              LEFT JOIN role on role.id = rm.role_id
              where u.user_id = %s  and m.id is not null
              )
            order by sort asc  
          """, [obj['id'],user_id])
        rows = cursor.fetchall()
      if rows:
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]
        ser = RoleMenuSerializer(instance=data, many=True,context={"user_id":user_id})
        return ser.data
      else :
        return []
  def get_meta(self, obj):
    ret = json.loads(obj['meta']) if obj['meta'] != None else None
    return ret

class SimpleRoleMenuSerializer(ModelSerializer):
  menu = MenuSerializer()
  class Meta:
    model=RoleMenu
    fields=["id","createTime","role","menu","half"]