# Generated by Django 5.1.2 on 2024-11-15 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_post_comments_remove_posts_posts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='members/'),
        ),
    ]
