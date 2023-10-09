from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f"User: name={self.name!r}, username={self.username!r}, email={self.email!r}"

    def __repr__(self):
        return str(self)

    # class Meta:
    #     ordering = ['username']


class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    body = models.TextField(blank=True, null=True)
    user_id = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"Post: title={self.title!r}, body={self.body!r}"

    def __repr__(self):
        return str(self)
