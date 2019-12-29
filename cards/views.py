from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from .forms import DeckForm
from .models import Deck


def decks(request):
    query_set = Deck.objects.order_by('-created_date').filter(is_active=True)
    context = {'decks': query_set}
    return render(request, 'decks.html', context)


@login_required()
def create_deck(request):
    # if request.method == "POST":
    #     title_input = request.POST.get('Form_title', None)
    #     description_input = request.POST.get('Form_description', None)
    #     if "Form_is_active" in request.POST:
    #         is_active_input = True
    #     else:
    #         is_active_input = False
    #
    #     if len(title_input) < 2:
    #         messages.info(request, 'Title is too short! It must have at least 2 chars')
    #         return HttpResponseRedirect('/decks/create')
    #     else:
    #         new_deck = Deck(title=title_input, description=description_input, is_active=is_active_input)
    #         new_deck.created_by = request.user
    #         new_deck.save()
    #         return HttpResponseRedirect('/decks/')
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
    deck_obj = get_object_or_404(Deck, id=deck_id, created_by=request.user)
    if request.method == "POST":
        form = DeckForm(request.POST, instance=deck_obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.info(request, f'Deck "{Deck.objects.get(id=deck_id)}" updated')
            return HttpResponseRedirect('/decks/')
    else:
        form = DeckForm(instance=deck_obj)
    context = {'form': form, 'edit_mode': True, 'deck_obj': deck_obj}
    return render(request, 'create_and_edit_deck.html', context)


@login_required()
def delete_deck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id, created_by=request.user)
    delete_name = Deck.objects.get(id=deck_id)
    deck_obj.delete()
    messages.info(request, f'Deck "{delete_name}" deleted')
    return HttpResponseRedirect('/decks/')


def view_deck(request, deck_id):
    deck_obj = get_object_or_404(Deck, id=deck_id)
    card_list = deck_obj.card_set.all()
    card_obj = card_list.first()
    print(deck_obj)
    print(card_list)
    print(card_obj)
    context = {'deck_obj': deck_obj, 'card_obj': card_obj}
    return render(request, 'view_deck.html', context)
