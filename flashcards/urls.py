from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users.views import main_page_view, register, login, logout, profile, ProfileUpdate, users_list, \
    change_user_status, about
from cards.views import decks, create_deck, edit_deck, delete_deck, view_deck, create_card, edit_card, delete_card, \
    view_cards

urlpatterns = [
    # users
    path('admin/', admin.site.urls),
    path('', main_page_view, name='home'),
    path('register/', register, name='register'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('profile-update/', ProfileUpdate.as_view(), name='profile-update'),
    path('users_list/', users_list, name='users_list'),
    path('change_status/<int:pk>/', change_user_status, name='change_status'),

    # cards
    path('decks/', decks, name='decks_name'),
    path('decks/create/', create_deck, name='create_deck_name'),
    path('decks/edit/<int:deck_id>', edit_deck, name='edit_deck_name'),
    path('decks/delete/<int:deck_id>', delete_deck, name='delete_deck_name'),
    path('decks/view/<int:deck_id>', view_deck, name='view_deck_name'),
    path('cards/create/<int:deck_id>', create_card, name='create_card_name'),
    path('cards/edit/<int:deck_id>/<int:card_id>', edit_card, name='edit_card_name'),
    path('cards/delete/<int:card_id>', delete_card, name='delete_card_name'),
    path('deck/view_cards/<int:deck_id>', view_cards, name='view_cards_name'),

    # REST FRAMEWORK URLS
    path('api/users/', include('users.api.urls', 'users_api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
