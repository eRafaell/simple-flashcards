from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Deck(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(max_length=128, null=False, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, default=None, blank=False, on_delete=models.CASCADE, null=True,
                                   related_name='deck_creator')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_num_of_cards(self):
        num = self.card_set.count()
        return str(num)

    get_num_of_cards.short_description = 'Card Count'


class Card(models.Model):
    parent_deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True)
    front = models.TextField()
    back = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, default=None, blank=False, on_delete=models.CASCADE, null=True,
                                   related_name='card_creator')

    def __str__(self):
        return self.front
