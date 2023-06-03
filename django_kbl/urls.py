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
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from scApp.views import user, depart, other, admin, account, task, order, chart, upload, city

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    path('index/', other.index),
    # path('user/list/', views.user_list),
    # path('user/add/', views.user_add),
    path('tpl/', other.tpl),
    path('news/', other.news),
    path('something/', other.something),

    # 用户登陆
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),
    path('login/list/', other.login_list),
    path('login/add/', other.login_add),
    path('login/del/', other.login_del),

    # 数据库操作
    path('orm/', other.orm),

    # ppt展示
    path('ppt/', other.ppt_view),

    # 部门列表
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/del/', depart.depart_del),
    path('depart/<int:nid>/edit/', depart.depart_edit),
    path('depart/multi/', depart.depart_multi),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/modelform/add/', user.user_modelform_add),
    path('user/<int:nid>/edit/', user.user_modelform_edit),
    path('user/<int:nid>/del/', user.user_modelform_del),

    # 管理员
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/del/', admin.admin_del),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 任务管理
    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),

    # 订单
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    path('order/tree/', order.order_tree),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),

    # 上传文件
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/modal/form/', upload.upload_modal_form),

    # 城市
    path('city/list/', city.city_list),
    path('city/add/', city.city_add),

]
