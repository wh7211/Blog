"""为应用程序users定义URL模式"""

# from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    # path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name="login"),

    # 注销
    url(r'^logout/$', views.logout_view, name='logout'),

    # 注册页面
    url(r'^register/$', views.register, name='register'),
]