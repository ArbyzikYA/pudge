# Generated by Django 3.1.4 on 2021-06-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_myuser_boost_unable'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='boosts_x10',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='boosts_x15',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='boosts_x8',
            field=models.BooleanField(default=False),
        ),
    ]
