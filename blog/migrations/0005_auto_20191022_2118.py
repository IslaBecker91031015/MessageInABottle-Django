# Generated by Django 2.2.6 on 2019-10-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191022_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='img/default.jpg', null=True, upload_to='data/media'),
        ),
    ]
