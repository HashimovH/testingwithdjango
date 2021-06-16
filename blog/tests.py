from django.test import TestCase
from .models import Post


# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title='First blog', author="Hashim", slug="first-blog")

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'First blog')
