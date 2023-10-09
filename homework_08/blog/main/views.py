from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy
from .models import User, Post
from .forms import UserCreateForm, PostCreateForm

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="main/index.html",
    )

class UsersList(ListView):
    model = User
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = "Users list"     
        return context
    
     
class UsersDetail(DetailView):
    model = User
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user_id=self.object.pk)
        return context
    

class UsersCreate(CreateView):
    model = User
    # fields = '__all__'
    form_class = UserCreateForm
    success_url = reverse_lazy('users')
    

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
