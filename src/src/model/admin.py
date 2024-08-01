from django.contrib import admin
from .Author import Author, AuthorAdmin
from .Book import Book, BookAdmin

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
