from django.urls import path
from .views import (
    users_list,
    index,
    posts_list,
    get_user_by_id,
    get_post_by_id,
)


urlpatterns = [
    path("", index),
    path("users/", users_list, name="users"),
    path("users/<int:user_id>/", get_user_by_id, name="user"),
    path("posts/", posts_list, name="posts"),
    path("posts/<int:post_id>/", get_post_by_id, name="post"),
]
