from django.http import HttpResponse
from django.urls import reverse
import json
# Create your views here.
def list(request):
  urls = reverse("x1:u")#别人的
  print(urls)

  print(request.path_info)
  print(request.GET)
  print(request.method)
  print(request.body)
  #print(request.resolver_match)

  print(request.POST)
  print(request.FILES.get("avatar"))
  print(request.headers)

  #json_data = json.loads(request.body)
  #print(json_data['name'])
  return HttpResponse("setting",content_type="application/json")