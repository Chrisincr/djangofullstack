# Generated by Django 2.1.7 on 2019-02-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvShows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
