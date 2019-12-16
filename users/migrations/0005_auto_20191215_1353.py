# Generated by Django 2.2 on 2019-12-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191213_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_user',
            field=models.TextField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
