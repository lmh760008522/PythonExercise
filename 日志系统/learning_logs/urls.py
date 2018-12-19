"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views
from django.urls import path

app_name='learning_logs'

urlpatterns = [
	#主页
	path('', views.index, name='index'),
	path('topics/', views.topics, name='topics'),
	#re_path(r'^topics/(?:(?P<topic_id>\d+)/)?$',views.topic,name='topic'),
	path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
	path('new_topic/', views.new_topic, name='new_topic'),
	path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
	path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
]