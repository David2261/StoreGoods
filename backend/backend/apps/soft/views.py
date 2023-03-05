from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .models import Menu, Category
from .utils import DataMixin


class MainPage(DataMixin, ListView):
	template_name = 'soft/main.html'
	model = Menu
	context_object_name = 'main'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		return dict(list(context.items()))

	def get_queryset(self):
		return Menu.objects.order_by('-pub_date').select_related('cat')


class SortPage(DataMixin, ListView):
	template_name = 'soft/main.html'
	model = Menu
	context_object_name = 'main'
	allow_empty = False

	def get_queryset(self):
		return Menu.objects.filter(
			cat__slug=self.kwargs['cat_slug'],
			).select_related('cat')

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c = Category.objects.get(slug=self.kwargs['cat_slug'])
		return dict(list(context.items()))


class MenuPage(DataMixin, DetailView):
	template_name = 'soft/detail.html'
	model = Menu
	slug_url_kwarg = 'slug'
	context_object_name = 'menu'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		return dict(list(context.items()))


