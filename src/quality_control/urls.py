from django.urls import include, path
from . import views


app_name = 'quality_control'

urlpatterns = [
	path('quality_control/', include([
		path('', views.IndexView.as_view(), name='index'),
		path('bugs/', views.bug_list, name='bug_list'),
		path('features/', views.feature_list, name='feature_list'),
		path('features/<int:feature_request_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
		path('bugs/<int:bug_report_id>/', views.BugDetailView.as_view(), name='bug_detail'),
	]))
]