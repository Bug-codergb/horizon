from django.db import models
from django.db.models import TextField
from apps.file.models import File

# Create your models here.
class Actor(models.Model):
  name= models.CharField(verbose_name="演员名称",max_length=125,null=False)
  description = models.TextField(verbose_name="简介",null=True)
  birthday = models.DateTimeField(null=True)
  birthplace = models.CharField(verbose_name="出生地",null=True,max_length=125)
  identity = models.CharField(verbose_name="身份",null=True,max_length=125)
  gender = models.IntegerField(verbose_name="性别",choices=((0,"男"),(1,"女")),default=0)
  nationality = models.CharField(verbose_name="国籍",max_length=125,null=True)
  people = models.CharField(verbose_name="民族",max_length=125,null=True)
  height = models.CharField(verbose_name="身高",max_length=125,null=True)
  constellation = models.CharField(verbose_name="星座",max_length=125,null=True)
  school = models.CharField(verbose_name="毕业学校",max_length=125,null=True)
  company = models.CharField(verbose_name="经济公司",max_length=125,null=True)
  avatar = models.ForeignKey(to=File,on_delete=models.SET_NULL,null=True)
  class Meta:
    db_table = "actor"
class ActorDeductive(models.Model):
  year = models.DateField(null=False)
  description = TextField(verbose_name="演绎经历描述")
  actor = models.ForeignKey(to="Actor",on_delete=models.CASCADE,null=False)
  class Meta:
    db_table = "actor_deductive"
class ActorMedia(models.Model):
  actor = models.ForeignKey(to=Actor,on_delete=models.CASCADE)
  file = models.ForeignKey(to=File,on_delete=models.CASCADE)
  class Meta:
    db_table = "actor_media"
