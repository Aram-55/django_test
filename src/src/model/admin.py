from django.contrib import admin
from .Author import Author,AuthorAdmin

admin.site.register(Author, AuthorAdmin)