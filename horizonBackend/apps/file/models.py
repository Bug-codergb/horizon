from django.utils import timezone
from django.db import models

# Create your models here.
class File(models.Model):
  url=models.CharField(max_length=255,null=True,unique=True)
  originalname=models.CharField(max_length=255,null=True)
  dest = models.CharField(max_length=125,null=True)
  filename = models.CharField(max_length=125,null=False)
  type = models.CharField(max_length=125,null=True)
  size =models.IntegerField(null=False)
  createTime = models.DateTimeField(default=timezone.now)
  updateTime = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = "file"