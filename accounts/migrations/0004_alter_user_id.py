# Generated by Django 3.2 on 2021-05-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210510_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default='b68f3a1b-0d98-4881-b685-2768cc76189c', primary_key=True, serialize=False),
        ),
    ]
