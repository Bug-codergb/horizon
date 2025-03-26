from django.db import models
from apps.file.models import File
class FilmCate(models.Model):
  name = models.CharField(max_length=225,null=False)
  createTime = models.DateTimeField(auto_now=True)
  meta = models.CharField(max_length=100,null=False,default='1')
  class Meta:
    db_table = "film_cate"

class Film(models.Model):
  name = models.CharField(verbose_name="名称",max_length=225,null=False,unique=True)
  foreign_name = models.CharField(max_length=225,null=True,unique=False)
  alias = models.CharField(max_length=225,null=True,unique=False)
  dt = models.IntegerField(default=0)
  language = models.CharField(max_length=125,null=True)
  cate = models.ManyToManyField(FilmCate,verbose_name="分类",through="FilmRelateCate"),
  cover = models.ForeignKey(verbose_name="封面",to=File,related_name="film_cover",on_delete=models.CASCADE)
  description = models.TextField(null=True)
  score = models.DecimalField(verbose_name="评分",max_digits=4,decimal_places=1)
  release_time = models.DateTimeField(verbose_name="上映时间",null=False)
  media = models.ManyToManyField(verbose_name="媒体文件",to=File,related_name="film_media",through="FilmVideo")
  # 继续创建结构
  class Meta:
    db_table="film"

class FilmRelateCate(models.Model):
  film = models.ForeignKey(to=Film,on_delete=models.CASCADE)
  cate = models.ForeignKey(to=FilmCate,on_delete=models.CASCADE)
  class Meta:
    db_table = "film_relate_cate"

class FilmVideo(models.Model):
  name = models.CharField(verbose_name="视频分类或简介",max_length=125)
  minitype = models.CharField(verbose_name="文件类型图片或者视频",max_length=100)
  file = models.ForeignKey(to=File,on_delete=models.CASCADE)
  film = models.ForeignKey(to=Film,on_delete=models.CASCADE)
  class Meta:
    db_table="film_video"