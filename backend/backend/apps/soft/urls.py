from django.urls import path

from .views import *

app_name = 'soft'
urlpatterns = [
	path('', MainPage.as_view(), name='main_page'),
	path('menu/<slug:cat_slug>/', SortPage.as_view(), name='sort_page'),
	path('menu/<slug:slug>/', MenuPage.as_view(), name='menu_page'),
]

