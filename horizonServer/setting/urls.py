from django.urls import path
from .views.config import list
urlpatterns = [
 path("config",list)
]
app_name="setting"