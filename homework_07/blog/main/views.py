from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import User, Post

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="main/index.html",
    )


def users_list(request: HttpRequest) -> HttpResponse:
    users = (
        User
        .objects
        .order_by("pk")
        .all()
    )
    return render(
        request=request,
        template_name="users/users.html",
        context={"users": users},
    )


def posts_list(request: HttpRequest) -> HttpResponse:
    posts = (
        Post
        .objects
        .order_by("pk")
        .all()
    )
    return render(
        request=request,
        template_name="posts/posts.html",
        context={"posts": posts},
    )
