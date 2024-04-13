from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from .models import BugReport, FeatureRequest


# def index(request):
# 	bugs_url = reverse('quality_control:bug_list')
# 	features_url = reverse('quality_control:feature_list')

# 	h1 = '<h1>Система контроля качества</h1>'
# 	bugs_a = f'<a href="{bugs_url}">Список всех багов</a>'
# 	features_a = f'<br><a href="{features_url}">Запросы на улучшение</a>'
# 	html = h1 + bugs_a + features_a

# 	return HttpResponse(html)


class IndexView(View):
	def get(self, request, *args, **kwargs):
		bugs_url = reverse('quality_control:bug_list')
		features_url = reverse('quality_control:feature_list')

		h1 = '<h1>Система контроля качества</h1>'
		bugs_a = f'<a href="{bugs_url}">Список всех багов</a>'
		features_a = f'<br><a href="{features_url}">Запросы на улучшение</a>'
		html = h1 + bugs_a + features_a

		return HttpResponse(html)


def bug_list(request):
	html = '<h1>Cписок отчетов об ошибках</h1><ul>'

	bugs = BugReport.objects.all()		

	for bug in bugs:
		statuses = bug.STATUS_CHOICES
		html += f'<li><a href="{bug.id}/">{bug.title}</a>: {statuses[bug.status]}</li>'

	html += '</ul>'

	return HttpResponse(html)


class BugDetailView(DetailView):
	model = BugReport
	pk_url_kwarg = 'id'


	def get(self, request, *args, **kwargs):
		self.object = self.get_object()

		bug = self.object
		project = bug.project
		task = bug.task
		statuses = bug.STATUS_CHOICES
		priorities = bug.PRIORITY_CHOICES

		project_url = reverse('tasks:project_detail', args=(project.id,))
		if task:
			task_url = reverse('tasks:task_detail', args=(task.project.id, task.id))

		html = f'<h1>Название: {bug.title}</h1><h3>Описание: {bug.description}</h3>'
		html += f'<p>Статус: {statuses[bug.status]}</p>'
		html += f'<p>Приоритет: {priorities[bug.priority]}</p><br>'
		html += f'<h2>Проект:</h2>'
		html += f'<a href="{project_url}">{project.name}</a>'
		html += f'<br><h2>Задача:</h2>'
		if task:
			html += f'<a href="{task_url}">{task.name}</a>'
		else:
			html += '<p>Задачи не прикреплено</p>'

		return HttpResponse(html)


def feature_list(request):
	html = '<h1>Список запросов на улучшение</h1><ul>'

	features = FeatureRequest.objects.all()

	for feature in features:
		statuses = feature.STATUS_CHOICES
		html += f'<li><a href="{feature.id}/">{feature.title}</a>: {statuses[feature.status]}</li>'

	html += '</ul>'

	return HttpResponse(html)


class FeatureDetailView(DetailView):
	model = FeatureRequest
	pk_url_kwarg = 'id'


	def get(self, request, *args, **kwargs):
		self.object = self.get_object()

		feature = self.object
		project = feature.project
		task = feature.task
		statuses = feature.STATUS_CHOICES
		priorities = feature.PRIORITY_CHOICES

		project_url = reverse('tasks:project_detail', args=(project.id,))
		if task:
			task_url = reverse('tasks:task_detail', args=(task.project.id, task.id))

		html = f'<h1>Название: {feature.title}</h1><h3>Описание: {feature.description}</h3>'
		html += f'<p>Статус: {statuses[feature.status]}</p>'
		html += f'<p>Приоритет: {priorities[feature.priority]}</p><br>'
		html += f'<h2>Проект:</h2>'
		html += f'<a href="{project_url}">{project.name}</a>'
		html += f'<br><h2>Задача:</h2>'
		if task:
			html += f'<a href="{task_url}">{task.name}</a>'
		else:
			html += '<p>Задачи не прикреплено</p>'

		return HttpResponse(html)