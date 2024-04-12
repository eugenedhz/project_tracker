from django.http import HttpResponse
from django.urls import reverse


def index(request):
	another_page_url = reverse('tasks:another_page')
	quality_control_url = reverse('quality_control:index')

	h1 = '<h1>Страница приложения tasks</h1>'
	another_page_a = f'<a href="{another_page_url}">Перейти на другую страницу</a>'
	quality_control_a = f'<br><a href="{quality_control_url}">Перейти на страницу контроля качества</a>'
	html = h1 + another_page_a + quality_control_a

	return HttpResponse(html)


def another_page(request):
	return HttpResponse('Это другая страница приложения tasks.')