from django.db import models
from apps.file.models import File
class FilmCate(models.Model):
  name = models.CharField(max_length=225,null=False)
  createTime = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = "film_cate"

class Film(models.Model):
  name = models.CharField(verbose_name="名称",max_length=225,null=False,unique=True)
  foreign_name = models.CharField(max_length=225,null=True,unique=False)
  alias = models.CharField(max_length=225,null=True,unique=False)
  dt = models.IntegerField(max_length=20,default=0)
  language = models.CharField(max_length=125,null=True)
  cate = models.ManyToManyField(verbose_name="分类",to=FilmCate,through="FileRelateCate"),
  cover = models.ForeignKey(verbose_name="封面",to=File,on_delete=models.CASCADE)
  description = models.TextField(null=True)
  score = models.DecimalField(verbose_name="评分",max_digits=4,decimal_places=1)
  release_time = models.DateTimeField(verbose_name="上映时间",null=False)
  # 继续创建结构
  class Meta:
    db_table="film"

class FileRelateCate(models.Model):
  film = models.ForeignKey(to=Film,on_delete=models.CASCADE)
  cate = models.ForeignKey(to=FilmCate,on_delete=models.CASCADE)
  class Meta:
    db_table = "film_relate_cate"