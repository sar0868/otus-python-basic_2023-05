from django import forms
from django.forms import ModelForm


from .models import User, Post

class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
