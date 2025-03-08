from django.db import models
from apps.role.models import Role

class Menu(models.Model):
  name = models.CharField(max_length=125,null=False,unique=True)
  path = models.CharField(max_length=123,null=False,unique=True)
  component = models.CharField(max_length=123,null=False,unique=False)
  meta = models.TextField(null=True)
  sort = models.IntegerField(default=0,null=False)
  parent = models.ForeignKey("self",on_delete=models.CASCADE,null=True,related_name="children")
  createTime = models.DateTimeField(auto_now=True)
  roles = models.ManyToManyField(Role,through="RoleMenu")
  class Meta:
    db_table = "menu"

class RoleMenu(models.Model):
  role = models.ForeignKey(Role,on_delete=models.CASCADE)
  menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
  createTime = models.DateTimeField(auto_now=True)
  half = models.IntegerField(null=False,default=0)
  class Meta:
    unique_together = (('role'),('menu'))
    db_table="role_menu"