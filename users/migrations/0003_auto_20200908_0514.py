# Generated by Django 3.1 on 2020-09-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200903_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
