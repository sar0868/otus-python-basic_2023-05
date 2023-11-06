from typing import Any
from django.db import models
from django.db.models import QuerySet
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy
from .models import Author, Post
from .forms import AuthorCreateForm, PostCreateForm

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="main/index.html",
    )


class AuthorsList(ListView):
    model = Author

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "Authors list"
        return context


class AuthorsDetail(DetailView):
    model = Author

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author_id=self.object.pk)
        return context


class AuthorsCreate(CreateView):
    model = Author
    # fields = '__all__'
    form_class = AuthorCreateForm
    success_url = reverse_lazy('authors')


class PostsList(ListView):
    model = Post

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['posts_list'] = "Posts list"
        context['title'] = "Posts list"
        return context


class PostsDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        return context


class PostsCreate(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('posts')
