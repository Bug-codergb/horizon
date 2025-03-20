from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from apps.cinema.models import Cinema
from apps.cinema.serializers.cinema import CinemaSerializer
from utils.response import RetResponse
from utils.pagination import CustomPageNumberPagination

class CinemaView(APIView):
  authentication_classes = []
  def post(self,request):
    name = request.data.get("name")
    alias = request.data.get("alias")
    address = request.data.get("address")
    userId = request.data.get("userId")
    print(userId)
    Cinema.objects.create(
      name=name,
      alias = alias,
      address = address,
      user_id = userId
    )
    return RetResponse.success(None,None)
class CinemaUserView(ListAPIView):
  authentication_classes = []
  serializer_class = CinemaSerializer
  pagination_class = CustomPageNumberPagination
  def get_queryset(self):
    user_id = self.kwargs.get("id")
    queryset = Cinema.objects.filter(user_id=user_id)
    return queryset