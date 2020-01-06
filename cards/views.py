from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from .forms import DeckForm, CardForm
from .models import Deck, Card


def decks(request):
    query_set = Deck.objects.order_by('-created_date').filter(is_active=True)
    context = {'decks': query_set}
    return render(request, 'decks.html', context)


@login_required()
def create_deck(request):

    if request.method == "POST":
        form = DeckForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.info(request, f'Deck "{Deck.objects.last()}" created')
            return HttpResponseRedirect('/decks/')
    else:
        form = DeckForm()
    context = {'form': form}
    return render(request, 'create_and_edit_deck.html', context)


@login_required()
def edit_deck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    if request.method == "POST":
        form = DeckForm(request.POST, instance=deck_obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.info(request, f'Deck "{Deck.objects.get(id=deck_id)}" was updated')
            return HttpResponseRedirect('/decks/')
    else:
        form = DeckForm(instance=deck_obj)
    context = {'form': form, 'edit_mode': True, 'deck_obj': deck_obj}
    return render(request, 'create_and_edit_deck.html', context)


@login_required()
def delete_deck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    delete_name = Deck.objects.get(id=deck_id)
    deck_obj.delete()
    messages.info(request, f'Deck "{delete_name}" deleted')
    return HttpResponseRedirect('/decks/')


def view_deck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    card_list = deck_obj.card_set.all()
    card_obj = card_list.first()
    if request.method == 'GET' and 'card' in request.GET:
        card_obj = get_object_or_404(Card, id=request.GET['card'])
    context = {'deck_obj': deck_obj, 'card_obj': card_obj}
    return render(request, 'view_deck.html', context)


def view_cards(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    card_list = deck_obj.card_set.all()
    context = {'deck_obj': deck_obj, 'card_list': card_list}
    return render(request, 'view_cards.html', context)


def create_card(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.parent_deck = Deck.objects.get(id=deck_id)
            instance.save()
            messages.info(request, f'New card in "{Deck.objects.get(id=deck_id)}" was created')
            return HttpResponseRedirect('/decks/')
    else:
        form = CardForm()
    context = {'form': form, 'deck_obj': deck_obj}
    return render(request, 'create_and_edit_card.html', context)


@login_required()
def edit_card(request, deck_id, card_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    card_obj = get_object_or_404(Card, id=card_id)
    if request.method == "POST":
        form = CardForm(request.POST, instance=card_obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.info(request, 'The card was updated')
            return HttpResponseRedirect('/decks/')
    else:
        form = CardForm(instance=card_obj)
    context = {'form': form, 'edit_mode': True, 'deck_obj': deck_obj, 'card_obj': card_obj}
    return render(request, 'create_and_edit_card.html', context)


@login_required()
def delete_card(request, card_id):
    card_obj = get_object_or_404(Card, id=card_id)
    delete_name = Card.objects.get(id=card_id)
    card_obj.delete()
    messages.info(request, f'Card "{delete_name}" deleted')
    return HttpResponseRedirect('/decks/')