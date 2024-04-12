from django.urls import include, path
from . import views


app_name = 'quality_control'

urlpatterns = [
	path('quality_control/', include([
		path('', views.index, name='index'),
		path('bugs/', views.bug_list, name='bug_list'),
		path('features/', views.feature_list, name='feature_list'),
		path('features/<int:id>/', views.feature_detail, name='feature_detail'),
		path('bugs/<int:id>/', views.bug_detail, name='bug_detail'),
	]))
]