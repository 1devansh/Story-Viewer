# Generated by Django 3.1.1 on 2020-09-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
