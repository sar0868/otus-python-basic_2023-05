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


def get_user_by_id(request: HttpRequest, user_id: int) -> HttpResponse:
    user = (
        User.objects.get(pk=user_id)
    )
    posts = (
        Post.objects.filter(user_id=user_id)
    )
    return render(
        request=request,
        template_name="users/detail.html",
        context={"user": user, "posts": posts},
    )


def posts_list(request: HttpRequest) -> HttpResponse:
    posts = (
        Post
        .objects
        .order_by("pk")
        .select_related("user_id")
        .all()
    )
    return render(
        request=request,
        template_name="posts/posts.html",
        context={"posts": posts},
    )


def get_post_by_id(request: HttpRequest, post_id: int) -> HttpResponse:
    post = (
        Post.objects.get(pk=post_id)
    )
    return render(
        request=request,
        template_name="posts/detail.html",
        context={"post": post},
    )
