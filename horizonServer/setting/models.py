from django.db import models
import datetime

class Setting(models.Model):
  name = models.CharField(
    verbose_name="名称",
    max_length=84,
    default="理想",
    null=False,
    blank=False,
    db_index=True,
    unique=True
  )
  gender = models.CharField(
    verbose_name="性别",
    choices=(('male','男'),('female','女')), # 对应关系
    default="male",
    max_length=111
  )
  sex=models.IntegerField(
    verbose_name="性别哈",
    choices=((1,"男"),(2,"女")),
    null=True
  )
  age = models.IntegerField(verbose_name="年龄")
  count = models.BigIntegerField(verbose_name="数量",default=1)
  create_time = models.DateField(verbose_name="日期",auto_now=True)
  #update_time = models.DateTimeField(verbose_name="时间",null=True)
  is_login = models.BooleanField(verbose_name="是否登录",default=False)
  money = models.DecimalField(verbose_name="金额",max_digits=10,decimal_places=2,null=True)



class User(models.Model):
  name = models.CharField(verbose_name="用户名",max_length=128)
  age = models.IntegerField(verbose_name="年龄")
  address = models.CharField(verbose_name="地址",max_length=128,null=True)
  gender = models.IntegerField(verbose_name="性别",choices=((1,"男"),(2,"女")),default=2)
  description=models.TextField(verbose_name="描述")
  create_time=models.DateField(verbose_name="创建时间",auto_now=True)
  #role = models.ForeignKey(verbose_name="角色",to="Role",to_field="id",on_delete=models.CASCADE)
  #role = models.ForeignKey(verbose_name="角色",to="Role",to_field="id",on_delete=models.SET_NULL,null=True)

class Role(models.Model):
  name =models.CharField(verbose_name="角色名称",max_length=128)
  create_time = models.DateField(verbose_name="创建时间",auto_now=True)

class Boy(models.Model):
  name=models.CharField(verbose_name="姓名",max_length=122)
  age = models.IntegerField(verbose_name="年",null=True)
class Girls(models.Model):
  name = models.CharField(verbose_name="姓名",max_length=122)
  relation= models.ManyToManyField(verbose_name="男女关系",to="Boy")