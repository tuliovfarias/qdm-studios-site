# Generated by Django 3.2.5 on 2021-08-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_photos_slide_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]