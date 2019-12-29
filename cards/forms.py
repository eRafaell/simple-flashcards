from django.forms import ModelForm
from .models import Deck

class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ['title', 'description', 'is_active']