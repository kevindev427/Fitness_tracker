# Generated by Django 3.0.5 on 2020-05-09 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nsfw',
            field=models.BooleanField(default=False),
        ),
    ]
