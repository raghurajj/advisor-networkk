# Generated by Django 3.2.1 on 2021-05-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_call_advisor_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='advisor_id',
            field=models.UUIDField(),
        ),
    ]
