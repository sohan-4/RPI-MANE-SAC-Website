# Generated by Django 5.1.2 on 2024-12-17 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]
