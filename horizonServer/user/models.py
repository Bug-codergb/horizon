from django.db import models
from django.forms import CharField


# Create your models here.
class Admin(models.Model):
  userId=models.CharField(verbose_name="用户名id",max_length=124,db_index=True)
  userName = models.CharField(verbose_name="用户名程",max_length=128,unique=True,null=False)
  dept = models.ForeignKey(to="Department",on_delete=models.CASCADE,to_field="id")
class Department(models.Model):
  name=models.CharField(verbose_name="部门名称",max_length=124,null=False,unique=True)

