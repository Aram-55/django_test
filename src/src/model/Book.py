from django.contrib import admin
from django.db import models
from .Author import Author
from django.utils.html import format_html


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pagination = models.IntegerField()

    def __str__(self):
        return self.name

    def author_info(self):
        link = "./admin/model/author/{}/change/"
        return format_html(
            '<a href="{}">{}</a>'.format(link,self.id)
        )



class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "author_info", "name", "pagination")
    search_fields = ("id", "name")


