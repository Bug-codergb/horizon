from .views.film import CreateFilmView,FilmListView,SetFilmCateView
from django.urls import path
from .views.category import CreateFilmCateView,FilmCateListView,FilmCateDeleteView
urlpatterns=[
  path("create",CreateFilmView.as_view()),
  path("cate/create",CreateFilmCateView.as_view()),
  path("cate/list",FilmCateListView.as_view()),
  path("cate/delete/<str:pk>",FilmCateDeleteView.as_view()),
  path("list",FilmListView.as_view()),
  path("cate",SetFilmCateView.as_view())
]
app_name="film"