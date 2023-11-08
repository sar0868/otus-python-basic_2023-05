from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import AuthorCreateForm, PostCreateForm
from .models import Author, Post


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
    success_url = reverse_lazy('main:authors')


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
    success_url = reverse_lazy('main:posts')


class PostsUpdate(UpdateView):
    model = Post
    template_name = 'main/post_form_edit.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('main:posts')


class PostsDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('main:posts')
