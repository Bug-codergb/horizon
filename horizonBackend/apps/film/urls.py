from .views.film import CreateFilmView
from django.urls import path
urlpatterns=[
  path("create",CreateFilmView.as_view())
]
app_name="film"