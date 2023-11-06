from django.urls import path
from .views import (
    index,
    AuthorsList,
    AuthorsDetail,
    AuthorsCreate,
    PostsList,
    PostsDetail,
    PostsCreate,
)

urlpatterns = [
    path("", index, name="home_page"),
    path("authors/", AuthorsList.as_view(), name="authors"),
    path("authors/add_author/", AuthorsCreate.as_view(), name='add_author'),
    path("authors/<slug:pk>/", AuthorsDetail.as_view(), name="author"),
    path("posts/", PostsList.as_view(), name="posts"),
    path("posts/add/", PostsCreate.as_view(), name="add_post"),
    path("posts/<slug:pk>/", PostsDetail.as_view(), name="post"),
]
