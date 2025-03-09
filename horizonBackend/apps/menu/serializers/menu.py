from rest_framework.serializers import ModelSerializer,SerializerMethodField
from apps.menu.models import Menu
import json
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