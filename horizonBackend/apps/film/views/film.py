from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from apps.film.models import Film
from utils.pagination import CustomPageNumberPagination
from utils.response import RetResponse
from apps.film.serializers.film import FilmSerializer
from apps.film.models import FilmRelateCate

class CreateFilmView(APIView):
  authentication_classes = []
  def post(self,request):
    data = request.data
    Film.objects.create(
      name=data.get("name"),
      foreign_name=data.get("foreign_name"),
      alias = data.get("alias"),
      dt = data.get("dt"),
      language = data.get("language"),
      description = data.get("description"),
      release_time = data.get("release_time"),
      cover_id = data.get("cover_id"),
      score = data.get("score")
    )
    return RetResponse.success(None,None)

class FilmListView(ListAPIView):
  authentication_classes = []
  queryset = Film.objects.all()
  pagination_class = CustomPageNumberPagination
  serializer_class = FilmSerializer

class SetFilmCateView(APIView):
  authentication_classes = []
  def post(self,request):
    film = request.data.get("film")
    cate = request.data.get("cate")

    FilmRelateCate.objects.filter(film_id = film).delete()
    l=[]
    for index,cate_id in enumerate(cate):
      l.append(FilmRelateCate(film_id = film,cate_id = cate_id))
    FilmRelateCate.objects.bulk_create(l)
    return RetResponse.success(None,None)