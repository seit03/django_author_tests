from multiprocessing.connection import Client

from django.test import TestCase

from django_books.models import Author, Books


class TestModelAuthor(TestCase):

    def test_create_author_model(self):
        author_info = {
            'name': 'TestName',
            'login': 'SEKA',
            'age': 24,
            'gender': 1,
            'nationality': 'nationality',
        }
        author = Author.objects.create(**author_info)
        self.assertEqual(author.name, author_info['name'])
        self.assertEqual(author.login, author_info['login'])
        self.assertEqual(author.age, author_info['age'])
        self.assertEqual(author.gender, author_info['gender'])
        self.assertEqual(author.nationality, author_info['nationality'])

    def test_create_fail_author_model(self):
        author_info = {
            'name': 'TestName',
            'login': 'SEKA',
            'age': 24,
            'gender': 1,
            'nationality': 'nationality',
        }
        with self.assertRaises(ValueError):
            author = Author.objects.create(**author_info)

    def test_update_author_model(self):
        author_info = {
            'name': 'Token',
            'login': 'SEKA',
            'age': 24,
            'gender': 1,
            'nationality': 'nationality',
        }
        new_login = 'WRITER'
        author = Author.objects.create(**author_info)
        author.login = new_login
        author.save()
        author.refresh_from_db()
        self.assertEqual(author.login, new_login)

    def test_delete_author_model(self):
        author_info = {
            'name': 'Token',
            'login': 'SEKA',
            'age': 24,
            'gender': 1,
            'nationality': 'nationality',
        }
        author = Author.objects.create(**author_info)
        pk = author.pk
        author.delete()
        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(pk=pk)


class TestModelBooks(TestCase):

    def test_create_books_model(self):
        author_info = {
            'name': 'TestName',
            'login': 'LIFE',
            'age': 24,
            'gender': 1,
            'nationality': 'nationality',
        }
        author = Author.objects.create(**author_info)
        client = Client()
        response = client.get(path=f'/author/{author.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_create_fail_books_model(self):
        author_info = {
            'name': 'TestName',
            'login': 'LIFE',
            'age': 24,
            'gender': 1,
            'nationality': 'nationality',
        }
        with self.assertRaises(ValueError):
            author = Author.objects.create(**author_info)

    def test_update_books_model(self):
        author_info = {
            'name': 'Token',
            'login': 'SEKA',
            'age': 24,
            'gender': 1,
            'nationality': 'nationality',
        }
        new_login = 'WRITER'
        author = Author.objects.create(**author_info)
        author.login = new_login
        author.save()
        author.refresh_from_db()
        self.assertEqual(author.login, new_login)

    def test_delete_books_model(self):
        author_info = {
            'name': 'Token',
            'login': 'SEKA',
            'age': 24,
            'gender': 1,
            'nationality': 'nationality',
        }
        author = Author.objects.create(**author_info)
        pk = author.pk
        author.delete()
        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(pk=pk)


class TestViews(TestCase):
    def test_get(self):
        pass
