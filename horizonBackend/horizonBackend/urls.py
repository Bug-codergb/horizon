from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from apps.login.views import LoginView
from apps.register.views import RegisterView
from apps.logout.views import LogoutView
urlpatterns = [
  path("user/",include("apps.user.urls",namespace="user")),
  path("file/",include("apps.file.urls",namespace="file")),
  path("role/",include("apps.role.urls",namespace="role")),
  path("menu/",include("apps.menu.urls",namespace="menu")),
  path("login",LoginView.as_view()),
  path("register",RegisterView.as_view()),
  path("logout",LogoutView.as_view()),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
