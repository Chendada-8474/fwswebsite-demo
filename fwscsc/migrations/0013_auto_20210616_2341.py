# Generated by Django 3.2.4 on 2021-06-16 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fwscsc', '0012_recruitment_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailcampro',
            name='dayIframeTag',
        ),
        migrations.RemoveField(
            model_name='trailcampro',
            name='nightIframeTag',
        ),
    ]
