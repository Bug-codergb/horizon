from django.urls import path
from .views.cinema import CinemaView,CinemaUserView
from .views.tag import CreateTagView,CreateCinemaTag
urlpatterns=[
  path("create",CinemaView.as_view()),
  path("tag/create",CreateTagView.as_view()),
  path("tag",CreateCinemaTag.as_view()),
  path("user/<str:id>",CinemaUserView.as_view())
]
app_name="cinema"