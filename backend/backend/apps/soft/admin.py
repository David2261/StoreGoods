from django.contrib import admin
from .models import Menu, Category
from datetime import datetime


class MenuAdmin(admin.ModelAdmin):
	list_display = ("name", "pub_date")
	prepopulated_fields = {"slug": ("name",)}
	readonly_field = ('time_update', 'slug', 'pub_date',)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('id', 'name')
	search_fields = ('name',)
	prepopulated_fields = {"slug": ("name",)}


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)