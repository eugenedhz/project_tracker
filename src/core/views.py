from django.views import View
from django.shortcuts import render


class IndexView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'base/base.html')