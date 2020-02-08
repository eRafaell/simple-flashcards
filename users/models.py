from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from PIL import Image


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics', null=True, blank=True)
    about_user = models.TextField(max_length=600, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    # zmniejsza rozmiar obrazka
    # def save(self, force_insert=False, force_update=False, using=None):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)



