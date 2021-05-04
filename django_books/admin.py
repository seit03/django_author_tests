from django.contrib import admin

# Register your models here.
from django_books.models import Author, Books

admin.site.register(Author)
admin.site.register(Books)
