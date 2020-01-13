from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from .forms import DeckForm, CardForm
from .models import Deck, Card


def decks(request):
    query_set_list = Deck.objects.order_by('-created_date').filter(is_active=True)
    if request.user.is_authenticated:
        logged_in_user_decks_list = Deck.objects.order_by('-created_by').filter(created_by=request.user)

        paginator = Paginator(query_set_list, 8)
        page_request_variable = 'page2'
        page = request.GET.get(page_request_variable)
        try:
            query_set = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            query_set = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            query_set = paginator.page(paginator.num_pages)

        paginator = Paginator(logged_in_user_decks_list, 2)
        page_request_var = 'page'
        page = request.GET.get(page_request_var)
        try:
            logged_in_user_decks = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            logged_in_user_decks = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            logged_in_user_decks = paginator.page(paginator.num_pages)

        context = {'decks': query_set,
                   'logged_in_user_decks': logged_in_user_decks,
                   'page_request_variable': page_request_variable,
                   'page_request_var': page_request_var
                   }
    else:
        context = {'decks': query_set_list}

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

    paginator = Paginator(card_list, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_set = paginator.page(paginator.num_pages)

    context = {'deck_obj': deck_obj, 'card_list': query_set, 'page_request_var': page_request_var}
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
