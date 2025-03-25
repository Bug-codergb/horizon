from django.db import models
from apps.file.models import File
from apps.user.models import User
# 影院标签
class CinemaTag(models.Model):
  name=models.CharField(null=False,max_length=225)
  createTime = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = "cinema_tag"

# 影院信息
class Cinema(models.Model):
  name=models.CharField(verbose_name="影院名称",null=False,max_length=225)
  alias = models.CharField(verbose_name="别名",null=True,max_length=500)
  address = models.CharField(verbose_name="影院地址",null=False,max_length=500)
  createTime = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True)
  tag = models.ManyToManyField(CinemaTag,through="CinemaRelateTag")
  class Meta:
    db_table = "cinema"

# 影院标签关联表
class CinemaRelateTag(models.Model):
  cinema = models.ForeignKey(to=Cinema,on_delete=models.CASCADE)
  tag = models.ForeignKey(to = CinemaTag,on_delete=models.CASCADE)
  createTime = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = "cinema_relate_tag"
# 影厅
class CinemaHall(models.Model):
  name=models.CharField(verbose_name="影厅名称",null=False,max_length=225)
  language = models.CharField(verbose_name="影厅语种",null=False,max_length=125)
  seat = models.CharField(verbose_name="座位图",null=False,max_length=225)
  cinema = models.ForeignKey(to=Cinema,on_delete=models.CASCADE)
  class Meta:
    db_table = "cinema_hall"
# 观影小吃
class CinemaFood(models.Model):
  name = models.CharField(verbose_name="名称",null=False,max_length=225)
  old_price = models.DecimalField(verbose_name="原价",null=False,max_digits=10,decimal_places=2)
  new_price = models.DecimalField(verbose_name="现价",null=False,max_digits=10,decimal_places=2)
  args= models.CharField(verbose_name="参数",max_length=500,null=False)
  cover = models.ForeignKey(to=File,on_delete=models.SET_NULL,null=True)
  is_delete = models.IntegerField(default=0,null=False,verbose_name="是否删除")
  cinema = models.ForeignKey(to=Cinema, on_delete=models.CASCADE)
  class Meta:
    db_table = "cinema_food"
# 小吃订单
class CinemaFoodOrder(models.Model):
  count = models.IntegerField(null=False)
  user = models.ForeignKey(to=User,on_delete=models.CASCADE)
  createTime = models.DateTimeField(auto_now=True)
  food = models.ForeignKey(to=CinemaFood,on_delete=models.CASCADE)
  class Meta:
    db_table = "cinema_food_order"
