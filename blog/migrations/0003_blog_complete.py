# Generated by Django 2.2 on 2019-08-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]