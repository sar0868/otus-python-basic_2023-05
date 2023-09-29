from django.contrib import admin

from .models import User, Post


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "username", "email"
    list_display_links = "pk", "username"


@admin.register(Post)
class PostrAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "body", "user_id"
    list_display_links = "pk", "title"
