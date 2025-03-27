from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from apps.actor.models import Actor
from utils.pagination import CustomPageNumberPagination
from utils.response import RetResponse
from apps.actor.models import Actor,ActorDeductive
from ..serializer.actor import ActorSerializer

class CreateActorView(APIView):
  authentication_classes = []
  def post(self,request):
    data = request.data
    Actor.objects.create(**data)
    return RetResponse.success(None,None)

class CreateDeductiveView(APIView):
  authentication_classes = []
  def post(self,request):
    year = request.data.get("year")
    description = request.data.get("description")
    actor_id = request.data.get("actor_id")
    ActorDeductive.objects.create(year=year,description=description,actor_id=actor_id)
    return RetResponse.success(None, None)

class ActorListView(ListAPIView):
  authentication_classes = []
  queryset = Actor.objects.all()
  serializer_class = ActorSerializer
  pagination_class = CustomPageNumberPagination