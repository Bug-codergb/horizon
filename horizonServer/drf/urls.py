from django.urls import path
from drf.views import demo,UserView
urlpatterns = [
  path("demo",demo),
  path("view/<int:id>",UserView.as_view())
]
app_name="drf"