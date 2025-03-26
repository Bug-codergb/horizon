from rest_framework.serializers import ModelSerializer
from apps.film.models import FilmCate,FilmRelateCate

class FilmCateSerializer(ModelSerializer):
  class Meta:
    model= FilmCate
    fields="__all__"

class FilmRelateCateSerializer(ModelSerializer):
    cate = FilmCateSerializer()
    class Meta:
      model = FilmRelateCate
      fields =['cate']