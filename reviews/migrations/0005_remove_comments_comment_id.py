# Generated by Django 3.2rc1 on 2021-07-11 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_comments_comment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_id',
        ),
    ]
