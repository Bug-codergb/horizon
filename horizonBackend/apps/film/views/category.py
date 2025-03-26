from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.views import APIView

from apps.film.serializers.category import FilmCateSerializer
from utils.response import RetResponse
from apps.film.models import FilmCate
from utils.pagination import CustomPageNumberPagination

class CreateFilmCateView(APIView):
  authentication_classes = []
  def post(self,request):
    name = request.data.get("name")
    FilmCate.objects.create(name = name)
    return RetResponse.success(None,None)

class FilmCateListView(ListAPIView):
  authentication_classes = []
  queryset = FilmCate.objects.all()
  serializer_class = FilmCateSerializer
  pagination_class = CustomPageNumberPagination

class FilmCateDeleteView(DestroyAPIView):
  authentication_classes = []
  queryset = FilmCate.objects.all()
  serializer_class = FilmCateSerializer
  pagination_class = CustomPageNumberPagination