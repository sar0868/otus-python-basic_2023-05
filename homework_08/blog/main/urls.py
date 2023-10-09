from django.urls import path
from .views import (
    index,
    UsersList,
    UsersDetail,
    UsersCreate,
    PostsList,
    PostsDetail,
    PostsCreate,
)

urlpatterns = [
    path("", index, name="home_page"),
    path("users/", UsersList.as_view(), name="users"),
    path("users/add_user/", UsersCreate.as_view(), name='add_user'),
    path("users/<slug:pk>/", UsersDetail.as_view(), name="user"),
    path("posts/", PostsList.as_view(), name="posts"),
    path("posts/add/", PostsCreate.as_view(), name="add_post"),
    path("posts/<slug:pk>/", PostsDetail.as_view(), name="post"),
]
