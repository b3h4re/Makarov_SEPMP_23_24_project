# Generated by Django 4.2.7 on 2023-11-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='about',
            field=models.TextField(default=''),
        ),
    ]
