# Generated by Django 2.2 on 2019-12-12 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191212_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profile_pics', verbose_name='default.jpg'),
        ),
    ]
