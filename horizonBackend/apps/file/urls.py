from django.urls import path
from .views.file import UploadView,DeleteFileView
urlpatterns=[
  path("upload",UploadView.as_view()),
  path("delete/<int:id>",DeleteFileView.as_view())
]
app_name="file"