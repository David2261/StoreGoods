from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .models import Menu


class MainPage(ListView):
	template_name = 'soft/main.html'
	model = Menu


class MenuPage(DetailView):
	template_name = 'soft/detail.html'
	model = Menu
	slug_url_kwarg = 'slug'
	context_object_name = 'menu'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title=context['menu'])
		return dict(list(context.items()) + list(c_def.items()))


