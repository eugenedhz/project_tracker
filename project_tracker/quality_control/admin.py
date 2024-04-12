from django.contrib import admin
from django.contrib.admin import actions
from django.utils.translation import gettext_lazy as _

from .models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
	list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
	readonly_fields = ('created_at', 'updated_at')
	list_filters = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
	search_fields = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')

	fieldsets = (
		(None, {
			'fields': ('title', 'description', 'status', 'priority')
		}),
		('Assign to', {
			'fields': ('project', 'task'),
			'classes': ('collapse',)
		}),
		('Dates', {
			'fields': ('created_at', 'updated_at'),
			'classes': ('collapse',)
		}),
	)

	actions = ['change_status_to_new', 'change_status_to_in_progress', 'change_status_to_completed']


	def change_status_to_new(self, request, queryset):
		queryset.update(status='New')


	def change_status_to_in_progress(self, request, queryset):
		queryset.update(status='In_progress')


	def change_status_to_completed(self, request, queryset):
		queryset.update(status='Completed')


	change_status_to_new.short_description = _('Change status to New')
	change_status_to_in_progress.short_description = _('Change status to In Progress')
	change_status_to_completed.short_description = _('Change status to Completed')



@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
	list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
	readonly_fields = ('created_at', 'updated_at')
	list_filters = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
	search_fields = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')

	fieldsets = (
		(None, {
			'fields': ('title', 'description', 'status', 'priority')
		}),
		('Assign to', {
			'fields': ('project', 'task'),
			'classes': ('collapse',)
		}),
		('Dates', {
			'fields': ('created_at', 'updated_at'),
			'classes': ('collapse',)
		}),
	)
