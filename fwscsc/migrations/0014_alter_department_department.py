# Generated by Django 3.2.4 on 2021-06-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwscsc', '0013_auto_20210616_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=15, null=True),
        ),
    ]