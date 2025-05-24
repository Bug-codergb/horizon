from django.urls import path
from .views.actor import CreateActorView,CreateDeductiveView,ActorListView,ActorDetailView
urlpatterns=[
  path("create",CreateActorView.as_view()),
  path("deductive/create",CreateDeductiveView.as_view()),
  path("list",ActorListView.as_view()),
  path("detail/<str:id>",ActorDetailView.as_view())
]
app_name="actor"