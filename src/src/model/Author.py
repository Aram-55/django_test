from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.html import format_html

GENDER_CHOICES = {
    "Male": "Male",
    "Female": "Female",
}


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "user_info", "age", "gender")
    search_fields = ("id", "age")

    def user_info(self, obj):
        link = "/admin/model/author/{}/change/".format(obj.user.id)
        return format_html(
            '<a href="{}">{}</a>'.format(link," ".join([obj.user.first_name,obj.user.last_name]))
        )

    user_info.short_description = "User"
