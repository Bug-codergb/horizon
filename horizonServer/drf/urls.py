from django.urls import path
from drf.views import demo,UserView,ParamsView,UserInfoView,AllUserInfoView
urlpatterns = [
  path("demo",demo),
  path("view/<int:id>",UserView.as_view()),
  path("params",ParamsView.as_view()),
  path("info",UserInfoView.as_view()),
  path("all",AllUserInfoView.as_view())
]
app_name="drf"