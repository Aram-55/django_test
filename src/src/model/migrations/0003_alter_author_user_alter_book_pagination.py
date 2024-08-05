# Generated by Django 5.0.7 on 2024-08-05 22:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_alter_author_gender_book'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='pagination',
            field=models.PositiveIntegerField(),
        ),
    ]
