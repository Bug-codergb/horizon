"""
URL configuration for horizonServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from web import views

urlpatterns = [
    # path("gb",views.home),
    # path("user/<int:userId>",views.user),
    # path("cater",views.cater),
    # path("login/<path:paths>",views.login)
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
