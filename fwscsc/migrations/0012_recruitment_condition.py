# Generated by Django 3.2.4 on 2021-06-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwscsc', '0011_recruitment_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='condition',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
