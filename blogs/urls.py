"""定义blogs的URL模式"""

# from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blogs'

urlpatterns = [
    # 主页
    # path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),

    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),

    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 用于编辑主题的页面
    url(r'^edit_topic/(?P<topic_id>\d+)/$', views.edit_topic, name='edit_topic'),


]