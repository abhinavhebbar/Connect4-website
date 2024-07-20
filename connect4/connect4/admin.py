from django.contrib import admin
from .models import Player, Game

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'wins')
    search_fields = ('username',)
    list_filter = ('wins',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'player1', 'player2', 'current_player_username')
    list_filter = ('player1', 'player2', 'current_player')
    search_fields = ('player1__username', 'player2__username', 'current_player__username')
from django.contrib import admin

# Register your models here.
