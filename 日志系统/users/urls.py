"""为应用程序users定义URL模式"""
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

LoginView.template_name = 'users/login.html'
app_name='users'

urlpatterns = [
	# 登录页面
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LoginView.as_view(), name='logout'),
	# 注册页面
	path('register/', views.register, name='register'),
]