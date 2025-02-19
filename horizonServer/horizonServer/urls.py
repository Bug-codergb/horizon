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
from django.urls import path,include
from web import views

urlpatterns = [
    # path("gb",views.home),
    # path("user/<int:userId>",views.user),
    # path("cater",views.cater),
    # path("login/<path:paths>",views.login)
    path("user/",include("user.urls"),name="user"),
    path("login/",include("login.urls"),name="login"),#server 内部跳转可以用到name
    path("setting/",include("setting.urls")),
    path("web/",include("web.urls")),
    path("movies/",include("apps.movies.urls")),
    path("cinema/",include("apps.cinema.urls")),
    path("reflect/",([
        path("demo1",views.reflect1,name="demo1"),
        path("demo2",views.reflect2),
                    ],None,None))
]
