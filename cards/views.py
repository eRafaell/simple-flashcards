from django.shortcuts import render
from .models import Deck


def decks(request):
    query_set = Deck.objects.order_by('-created_date').filter(is_active=True)
    context = {'decks': query_set}
    return render(request, 'decks.html', context)
