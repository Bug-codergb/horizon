from rest_framework.serializers import ModelSerializer,SerializerMethodField
from apps.film.models import Film
from apps.file.serializers.file import FileSerializer
from apps.film.serializers.category import FilmCateSerializer,FilmRelateCateSerializer
from apps.film.models import FilmRelateCate

class FilmSerializer(ModelSerializer):
  cover = FileSerializer()
  cate = SerializerMethodField()
  class Meta:
    model=Film
    fields=["id","name","foreign_name","alias","dt","language","description","score","release_time","cover","cate"]
  def get_cate(self,obj):
    categories = FilmRelateCate.objects.filter(film_id = obj.id)
    json = FilmRelateCateSerializer(instance=categories,many=True)
    category_list = [item["cate"] for item in json.data]
    return category_list
