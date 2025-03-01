from django.urls import path
from .views.config import list,DeleteView,rawDel,update,all
urlpatterns = [
 path("config",list),
 path("delete",DeleteView.as_view()),
 path("del/<int:id>",rawDel),
 path("update/<int:id>/<str:name>",update),
 path("all",all)
]
app_name="setting"