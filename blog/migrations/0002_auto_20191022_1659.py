# Generated by Django 2.2.6 on 2019-10-22 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='static/img/beach.jpg', null=True, upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='static/img/default.jpg', null=True, upload_to='static/img/'),
        ),
    ]
