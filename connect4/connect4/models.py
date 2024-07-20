from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    username = models.CharField(max_length=50, unique=True)
    wins = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Game(models.Model):
    player1 = models.ForeignKey(Player, related_name='player1_games', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='player2_games', on_delete=models.CASCADE)
    current_player = models.ForeignKey(Player, related_name='current_player_games', on_delete=models.CASCADE, default=None)

    @property
    def current_player_username(self):
        return self.current_player.username if self.current_player else None
