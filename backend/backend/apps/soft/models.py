from django.db import models
from django.urls import reverse


class Category(models.Model):
	name = models.CharField(verbose_name='Название', max_length=255)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

	def get_absolute_url(self):
		return reverse("soft:sort_page", kwargs={'cat_slug': self.slug})

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['id']


class Menu(models.Model):
	name = models.CharField(verbose_name='Название', max_length=255)
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
	time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
	cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

	def get_absolute_url(self):
		return reverse("soft:menu_page", kwargs={'slug': self.slug})

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Меню"
		verbose_name_plural= "Меню"
		ordering = ('-time_update', '-pub_date')
