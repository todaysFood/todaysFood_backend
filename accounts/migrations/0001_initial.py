# Generated by Django 3.2 on 2021-05-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default='741605de-89ba-4efb-8e21-e37c3a988ef5', primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=25, unique=True, verbose_name='User Email')),
                ('password', models.CharField(max_length=64, verbose_name='User Password')),
                ('name', models.CharField(max_length=15, verbose_name='Usr Name')),
                ('nick_name', models.CharField(max_length=15, verbose_name='User Nick Name')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Last Login Time')),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
