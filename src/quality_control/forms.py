from django.forms import ModelForm

from tasks.models import Task, Project
from .models import BugReport, FeatureRequest


class BaseForm:
	def __init__(self, *args, **kwargs):
		project_id = kwargs.pop('initial', {}).get('project_id')
		super().__init__(*args, **kwargs)
		print(project_id)
		if project_id:
			self.fields['task'].queryset = Task.objects.filter(project_id=project_id)


class BugReportForm(ModelForm, BaseForm):
	class Meta:
		model = BugReport
		fields = ['title', 'description', 'status', 'priority', 'task']


class FeatureRequestForm(ModelForm, BaseForm):
	class Meta:
		model = FeatureRequest
		fields = ['title', 'description', 'status', 'priority', 'task']