from django.urls import path
from .views.config import list,DeleteView
urlpatterns = [
 path("config",list),
 path("delete",DeleteView.as_view())
]
app_name="setting"