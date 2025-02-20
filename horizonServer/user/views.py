from django.http import HttpResponse
from django.shortcuts import render

def list(request):
  return HttpResponse("user-list")