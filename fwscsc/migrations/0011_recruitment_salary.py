# Generated by Django 3.2.4 on 2021-06-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fwscsc', '0010_auto_20210616_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitment',
            name='salary',
            field=models.CharField(max_length=50, null=True),
        ),
    ]