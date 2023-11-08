from django.urls import path
from .views import (
    index,
    AuthorsList,
    AuthorsDetail,
    AuthorsCreate,
    PostsList,
    PostsDetail,
    PostsCreate,
    PostsUpdate,
    PostsDelete,
)

app_name = "main"

urlpatterns = [
    path("", index, name="home_page"),
    path("authors/", AuthorsList.as_view(), name="authors"),
    path("authors/add_author/", AuthorsCreate.as_view(), name='add_author'),
    path("authors/<slug:pk>/", AuthorsDetail.as_view(), name="author"),
    path("posts/", PostsList.as_view(), name="posts"),
    path("posts/<int:pk>/edit/", PostsUpdate.as_view(), name="edit"),
    path("posts/<int:pk>/delete/", PostsDelete.as_view(), name="delete"),
    path("posts/add/", PostsCreate.as_view(), name="add_post"),
    path("posts/<slug:pk>/", PostsDetail.as_view(), name="post"),
]
