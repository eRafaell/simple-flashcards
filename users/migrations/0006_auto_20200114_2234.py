# Generated by Django 2.2 on 2020-01-14 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191215_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pics'),
        ),
    ]