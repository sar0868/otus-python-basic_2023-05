from django.test import TestCase, Client
# from django.urls import reverse

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

        for post in self.posts:
            author = Author.objects.get(username=post["author"])
            self.client.post(
                path='/posts/add/',
                data={
                    "title": post["title"],
                    "body": "simple text",
                    'author_id': author.pk
                }
            )
        self.client = Client()

    def test_create_post(self):
        posts_cnt = Post.objects.count()
        self.assertEqual(posts_cnt, 3)
        author = Author.objects.get(username="user1")
        responce = self.client.post(
            path='/posts/add/',
            data={
                "title": "post12",
                "body": "simple text",
                'author_id': author.pk
            }
        )
        self.assertNotEqual(200, responce.status_code)
        posts_cnt = Post.objects.count()
        self.assertEqual(posts_cnt, 4)

    def test_get_posts_by_user(self):
        author = Author.objects.get(username="user1")
        posts_cnt_by_user1 = Post.objects.filter(author_id= author.pk)
        self.assertEqual(len(posts_cnt_by_user1), 2)

    def test_path_update_post(self):
        response = self.client.get('/posts/2/edit/')
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        body_new = "new text"
        response = self.client.post(
            '/posts/1/edit/',
            data={
                "title": "post1",
                "body": body_new,
                'author_id': 1
            }
        )
        post = Post.objects.get(id=1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(post.body, body_new)

    def test_path_delete_post(self):
        response = self.client.get('/posts/2/delete/')
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        response = self.client.post(
            path="/posts/2/delete/",
        )
        self.assertEqual(response.status_code, 302)
        posts = Post.objects.all()
        self.assertEqual(len(posts), 2)
