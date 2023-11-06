from django.test import TestCase

from .models import Author, Post


# Create your tests here.
class PostTest(TestCase):

    def setUp(self):
        authors = [
            {"name": 'User1', 'username': 'user1', 'email': 'user1@mail.com'},
            {"name": 'User2', 'username': 'user2', 'email': 'user2@mail.com'},
        ]
        for el in authors:
            # self.client.post()
            Author.objects.create(
                name=el['name'],
                username=el['username'],
                email=el['email']
            )

        self.posts = [
            {"title": "post1", "author": "user1"},
            {"title": "post2", "author": "user1"},
            {"title": "post3", "author": "user2"},
        ]



    def test_create_post(self):
        posts_cnt = Post.objects.count()
        self.assertEqual(posts_cnt, 0)
        author = Author.objects.get(username="user1")
        responce = self.client.post(
            path='/posts/add/',
            data={
                "title": "post1",
                "body": "simple text",
                'author_id': author.pk
            }
        )
        self.assertNotEquals(200, responce.status_code)
        posts_cnt = Post.objects.count()
        self.assertEqual(posts_cnt, 1)

    def test_get_posts_by_user(self):
        for post in self.posts:
            author = Author.objects.get(username=post["author"])
            responce = self.client.post(
                path='/posts/add/',
                data={
                    "title": post["title"],
                    "body": "simple text",
                    'author_id': author.pk
                }
            )
        author = Author.objects.get(username="user1")
        posts_cnt_by_user1 = Post.objects.filter(author_id= author.pk)
        self.assertEqual(len(posts_cnt_by_user1), 2)
