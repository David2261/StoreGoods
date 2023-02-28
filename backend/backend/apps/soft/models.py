from django.db import models

# Create your models here.

class Menu(models.Model):
	name = models.CharField(title='Название', max_length=255)
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
	time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

	def get_absolute_url(self):
		return reverse("menu", kwargs={'slug': self.slug})

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Меню"
		verbose_name_plural= "Меню"
		ordering = ('-time_update', '-pub_date')