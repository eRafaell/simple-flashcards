# Generated by Django 2.2 on 2019-12-23 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0002_deck_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deck_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
