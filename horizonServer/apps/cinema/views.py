from django.http import HttpResponse
import json
# Create your views here.
def list(request):
  cinemaList=[]
  cinema1={
    "name":"万达影院",
    "address":"北京"
  }
  cinema2={
    "name":"华谊兄弟",
    "address":"上海"
  }
  cinemaList.append(cinema1)
  cinemaList.append(cinema2)
  json_date = json.dumps(cinemaList)
  return HttpResponse(json_date,content_type="application/json",charset="utf-8")