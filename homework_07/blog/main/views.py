from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import User, Post


# Create your views here.
def users_list(request: HttpRequest) -> HttpResponse:
    users = (
        User
        .objects
        .order_by("pk")
        .all()
    )
    return render(
        request=request,
        template_name="users/index.html",
        context={"users": users}
    )
