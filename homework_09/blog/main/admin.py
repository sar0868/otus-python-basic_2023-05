from django.contrib import admin

from .models import Author, Post


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "username", "email"
    list_display_links = "pk", "username"


@admin.register(Post)
class PostrAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "body", "author_id"
    list_display_links = "pk", "title"
