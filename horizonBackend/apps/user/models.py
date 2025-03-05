from django.db import models
from apps.file.models import File


class User(models.Model):
  user_id=models.CharField(primary_key=True,max_length=100)
  user_name = models.CharField(unique=True,max_length=255,null=False)
  gender = models.IntegerField(choices=((1,"男"),(0,"女")),default=0,null=False)
  password = models.CharField(unique=False,max_length=255,null=False)
  description = models.TextField(verbose_name="简介",null=True)
  avatar = models.ForeignKey(File,verbose_name="用户头像",on_delete=models.SET_NULL,null=True,db_column="avatar")
  class Meta:
    db_table = "user"