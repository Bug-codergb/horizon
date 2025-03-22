from rest_framework.views import APIView

from utils.response import RetResponse


class CreateFilmView(APIView):
  authentication_classes = []
  def post(self,request):
    return RetResponse.success(None,None)