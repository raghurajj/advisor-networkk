# Generated by Django 3.2.1 on 2021-05-07 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0004_rename_advisorprofile_advisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='profile_pic',
            field=models.URLField(),
        ),
    ]
