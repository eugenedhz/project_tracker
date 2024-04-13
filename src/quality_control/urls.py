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
		path('project/<int:project_id>/features/new/', views.create_feature_request, name='create_feature_request'),
		path('project/<int:project_id>/bugs/new/', views.create_bug_report, name='create_bug_report'),
		# path('project/<int:project_id>/bugs/<int:bug_report_id>/update', views.BugUpdateView.as_view(), name='update_bug'),
		path('project/<int:project_id>/bugs/<int:bug_report_id>/update', views.update_bug, name='update_bug'),
		# path('project/<int:project_id>/features/<int:feature_request_id>/update', views.FeatureUpdateView.as_view(), name='update_feature'),
		path('project/<int:project_id>/features/<int:feature_request_id>/update', views.update_feature, name='update_feature'),
		# path('bugs/<int:bug_report_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug_report'),
		path('bugs/<int:bug_report_id>/delete/', views.delete_bug_report, name='delete_bug_report'),
		# path('features/<int:feature_request_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature_request'),
		path('features/<int:feature_request_id>/delete/', views.delete_feature_request, name='delete_feature_request'),
	]))
]