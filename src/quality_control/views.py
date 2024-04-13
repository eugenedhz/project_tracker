from django.shortcuts import render
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
		return render(request, 'quality_control/index.html')


def bug_list(request):
	bugs = BugReport.objects.all()		

	return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})


class BugDetailView(DetailView):
	model = BugReport
	pk_url_kwarg = 'bug_report_id'
	template_name = 'quality_control/bug_detail.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['project'] = self.object.project
		context['task'] = self.object.task
		context['bug'] = self.object

		return context


def feature_list(request):
	features = FeatureRequest.objects.all()

	return render(request, 'quality_control/feature_list.html', {'feature_list': features})


class FeatureDetailView(DetailView):
	model = FeatureRequest
	pk_url_kwarg = 'feature_request_id'
	template_name = 'quality_control/feature_detail.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['project'] = self.object.project
		context['task'] = self.object.task
		context['feature'] = self.object

		return context
