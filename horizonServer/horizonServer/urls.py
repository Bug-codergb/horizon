from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from web import views

urlpatterns = [
    # path("gb",views.home),
    # path("user/<int:userId>",views.user),
    # path("cater",views.cater),
    # path("login/<path:paths>",views.login)
    path("drf/",include("drf.urls",namespace="x4")),
    path("user/",include("user.urls",namespace="x1")),#生成url时，使用x1:user反向生成
    path("login/",include("login.urls",namespace="x2")),#server 内部跳转可以用到name
    path("setting/",include("setting.urls",namespace="x3")),
    path("web/",include("web.urls")),
    path("movies/",include("apps.movies.urls")),
    path("cinema/",include("apps.cinema.urls")),
    path("reflect/",([
        path("demo1",views.reflect1,name="demo1"),
        path("demo2",views.reflect2),
                    ],None,None))
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
