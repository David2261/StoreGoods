from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
	list_display = ("name", "pub_date")
	prepopulated_fields = {"slug": ("name")}


admin.site.register(Menu, MenuAdmin)