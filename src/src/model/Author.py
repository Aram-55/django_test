from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

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

    def user_info(self):
        return self.user.username

    user_info.short_description = "User"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "user_info", "age", "gender")
    search_fields = ("id", "age")






