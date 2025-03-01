from django.urls import path
from user.views import list,create,createDept,userDept
urlpatterns = [
    path("list",list,name="u"),
    path("create",create),
    path("dept/create/<str:name>",createDept),
    path("dept",userDept)
]
app_name="user"
