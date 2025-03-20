from rest_framework.views import APIView
from apps.cinema.models import CinemaTag,CinemaRelateTag
from utils.response import RetResponse


class CreateTagView(APIView):
  authentication_classes = []
  def post(self,request):
    name = request.data.get("name")
    CinemaTag.objects.create(name=name)
    return RetResponse.success(None,None)

class CreateCinemaTag(APIView):
  authentication_classes = []
  def post(self,request):
    cinema_id = request.data.get("cinema_id")
    tag = request.data.get("tag")
    print(cinema_id)
    print(tag)
    CinemaRelateTag.objects.filter(cinema_id = cinema_id).delete()
    l=[]
    for index,tag_id in enumerate(tag):
      l.append(CinemaRelateTag(cinema_id = cinema_id,tag_id=tag_id))
    CinemaRelateTag.objects.bulk_create(l)
    return RetResponse.success(None, None)