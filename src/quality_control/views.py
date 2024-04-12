from django.http import HttpResponse
from django.urls import reverse


def index(request):
	bugs_url = reverse('quality_control:bug_list')
	features_url = reverse('quality_control:feature_list')

	h1 = '<h1>Система контроля качества</h1>'
	bugs_a = f'<a href="{bugs_url}">Список всех багов</a>'
	features_a = f'<br><a href="{features_url}">Запросы на улучшение</a>'
	html = h1 + bugs_a + features_a

	return HttpResponse(html)


def bug_list(request):
	return HttpResponse('<h1>Cписок отчетов об ошибках</h1>')


def feature_list(request):
	return HttpResponse('<h1>Список запросов на улучшение</h1>')


def bug_detail(request, id):
	return HttpResponse(f'Детали бага {id}')


def feature_detail(request, id):
	return HttpResponse(f'Детали улучшения {id}')
