from rest_framework.response import Response
from rest_framework.views import APIView
from apps.user.serializers.user import UserSerializer
from apps.user.models import User
from utils.general import generateID
import time
from utils.response import RetResponse

class CreateUser(APIView):
  def post(self,request):
    data= request.data
    id = generateID()
    User.objects.create(user_id=id,**data)
    return RetResponse.success(None,None)
