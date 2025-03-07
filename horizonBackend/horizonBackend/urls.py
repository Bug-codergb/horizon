from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
urlpatterns = [
  path("user/",include("apps.user.urls",namespace="user")),
  path("file/",include("apps.file.urls",namespace="file")),
  path("role/",include("apps.role.urls",namespace="role"))
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
