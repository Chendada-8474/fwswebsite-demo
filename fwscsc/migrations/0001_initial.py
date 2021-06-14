# Generated by Django 3.2.4 on 2021-06-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subTitle', models.CharField(max_length=50)),
                ('slogan', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=250)),
                ('brandImg', models.FilePathField()),
            ],
        ),
    ]
