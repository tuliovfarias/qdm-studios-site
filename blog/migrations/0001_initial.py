# Generated by Django 3.2.5 on 2021-07-15 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=3000)),
                ('date', models.DateTimeField()),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
    ]
