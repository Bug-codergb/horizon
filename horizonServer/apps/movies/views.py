from django.http import HttpResponse
# Create your views here.
def list(request):
  return HttpResponse("电影列表")