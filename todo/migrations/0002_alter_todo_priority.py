# Generated by Django 5.0.1 on 2024-01-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(default=3),
        ),
    ]