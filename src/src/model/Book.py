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


class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "author_info", "name", "pagination")
    search_fields = ("id", "name")

    def author_info(self, obj):
        link = "/admin/model/book/{}/change/".format(obj.author.id)
        return format_html(
            '<a href="{}">{}</a>'.format(link, " ".join([obj.author.user.first_name,obj.author.user.last_name]))
        )

    author_info.short_description = "Author"
