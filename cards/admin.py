from django.contrib import admin
from .models import Deck, Card

class DeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'get_num_of_cards')
    list_filter = ('is_active',)
    search_fields = ['title', 'description']

class CardAdmin(admin.ModelAdmin):
    pass

admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
