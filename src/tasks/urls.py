from django.urls import path

from . import views


app_name = 'tasks'

urlpatterns = [
	path('', views.index),
	path('another/', views.another_page, name='another_page'),
]