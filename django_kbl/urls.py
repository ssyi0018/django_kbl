"""
URL configuration for django_kbl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from scApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('tpl/', views.tpl),
    path('news/', views.news),
    path('something/', views.something),

    # 用户登陆
    path('login/', views.login),
    path('login/list/', views.login_list),
    path('login/add/', views.login_add),
    path('login/del/', views.login_del),

    # 数据库操作
    path('orm/', views.orm),

    # ppt展示
    path('ppt/', views.ppt_view),
]
