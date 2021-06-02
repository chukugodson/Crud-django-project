from django.contrib import admin
from . import models

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
	list_display = ["id", "username", "email"]
	list_filter = ["id", "username", "email"]
	search_fields = ["id", "username"]

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ["user", "name", "text", "date_published"]
	list_filter = ["user", "name", "text", "date_published"]
