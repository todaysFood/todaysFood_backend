# Generated by Django 3.2.2 on 2021-05-26 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_rename_author_posts_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='author_id',
        ),
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(db_column='author', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
