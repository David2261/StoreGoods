from django.urls import path

app_name = 'soft'
urlpatterns = [
	path('', MainPage.as_view(), name='main_page'),
	path('menu/<slug:slug>/', MenuPage.as_view(), name='menu_page'),
]

