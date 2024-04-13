from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView

from tasks.models import Project
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm


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


# class BugListView(ListView):
#     model = BugReport
#     template_name = 'quality_control/bug_list.html'


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


# def bug_detail(request, bug_report_id):
# 	bug = get_object_or_404(BugReport, id=bug_report_id)	
# 	task = bug.task
# 	project = bug.project

# 	return render(request, 'quality_control/bug_detail.html', {'bug': bug, 'task': task, 'project': project})


def feature_list(request):
	features = FeatureRequest.objects.all()

	return render(request, 'quality_control/feature_list.html', {'feature_list': features})


# class FeatureListView(ListView):
#     model = FeatureRequest
#     template_name = 'quality_control/feature_list.html'


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


# def feature_detail(request, feature_request_id):
# 	feature = get_object_or_404(FeatureRequest, id=feature_request_id)	
# 	task = feature.task
# 	project = feature.project

# 	return render(request, 'quality_control/feature_detail.html', {'feature': feature, 'task': task, 'project': project})


def create_bug_report(request, project_id):
	project = get_object_or_404(Project, pk=project_id)

	if request.method == 'POST':
		form = BugReportForm(request.POST or None, initial={'project_id': None})
		if form.is_valid():
			bug = form.save(commit=False)
			bug.project = project
			bug.save()
			return redirect('quality_control:bug_list')
	else:
		form = BugReportForm(initial={'project_id': project.id})

	return render(request, 'quality_control/bug_report_form.html', {'form': form, 'project': project})


# class BugReportCreateView(CreateView):
#     model = BugReport
#     form_class = BugReportForm
#     template_name = 'quality_control/bug_report_form.html'


#     def form_valid(self, form):
#         project_id = self.kwargs['project_id']
#         project = Project.objects.get(pk=project_id)
#         form.instance.project = project

#         return super().form_valid(form)


#     def get_success_url(self):
#         return reverse('quality_control:bug_list')


def create_feature_request(request, project_id):
	project = get_object_or_404(Project, pk=project_id)

	if request.method == 'POST':
		form = FeatureRequestForm(request.POST or None, initial={'project_id': None})
		if form.is_valid():
			feature = form.save(commit=False)
			feature.project = project
			feature.save()
			return redirect('quality_control:feature_list')
	else:
		form = FeatureRequestForm(initial={'project_id': project.id})

	return render(request, 'quality_control/feature_request_form.html', {'form': form, 'project': project})


# class FeatureRequestCreateView(CreateView):
#     model = FeatureRequest
#     form_class = FeatureRequestForm
#     template_name = 'quality_control/feature_request_form.html'

#     def form_valid(self, form):
#         project_id = self.kwargs['project_id']
#         project = Project.objects.get(pk=project_id)
#         form.instance.project = project
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse('quality_control:feature_list')


def update_bug(request, project_id, bug_report_id):
	project = get_object_or_404(Project, pk=project_id)
	bug = get_object_or_404(BugReport, pk=bug_report_id)

	if request.method == 'POST':
		form = BugReportForm(request.POST or None, initial={'project_id': None}, instance=bug)
		if form.is_valid():
			form.save()
			return redirect('quality_control:bug_detail', bug_report_id=bug.id)
	else:
		form = BugReportForm(initial={'project_id': project.id}, instance=bug)
	
	return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})


# class BugUpdateView(UpdateView):
# 	model = BugReport
# 	form_class = BugReportForm
# 	template_name = 'quality_control/bug_update.html'
# 	pk_url_kwarg = 'bug_report_id'

# 	def get_success_url(self):
# 		return reverse_lazy('quality_control:bug_detail', kwargs={'bug_report_id': self.object.id})


def update_feature(request, project_id, feature_request_id):
	project = get_object_or_404(Project, pk=project_id)
	feature = get_object_or_404(FeatureRequest, pk=feature_request_id)

	if request.method == 'POST':
		form = FeatureRequestForm(request.POST or None, initial={'project_id': None}, instance=feature)
		if form.is_valid():
			form.save()
			return redirect('quality_control:feature_detail', feature_request_id=feature.id)
	else:
		form = FeatureRequestForm(initial={'project_id': project.id}, instance=feature)
	
	return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})


# class FeatureUpdateView(UpdateView):
# 	model = FeatureRequest
# 	form_class = FeatureRequestForm
# 	template_name = 'quality_control/feature_update.html'
# 	pk_url_kwarg = 'feature_request_id'

# 	def get_success_url(self):
# 		return reverse_lazy('quality_control:feature_detail', kwargs={'feature_request_id': self.object.id})


def delete_bug_report(request, bug_report_id):
	bug = get_object_or_404(BugReport, pk=bug_report_id)
	bug.delete()

	return redirect('quality_control:bug_list')


# class BugDeleteView(DeleteView):
# 	model = BugReport
# 	pk_url_kwarg = 'bug_report_id'
# 	success_url = reverse_lazy('quality_control:bug_list')
# 	template_name = 'quality_control/bug_confirm_delete.html'


# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['bug'] = self.object

# 		return context


def delete_feature_request(request, feature_request_id):
	feature = get_object_or_404(FeatureRequest, pk=feature_request_id)
	feature.delete()

	return redirect('quality_control:feature_list')


# class FeatureDeleteView(DeleteView):
# 	model = FeatureRequest
# 	pk_url_kwarg = 'feature_request_id'
# 	success_url = reverse_lazy('quality_control:feature_list')
# 	template_name = 'quality_control/feature_confirm_delete.html'


# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['feature'] = self.object

# 		return context