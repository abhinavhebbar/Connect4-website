from django.shortcuts import render,redirect
from .models import Player, Game
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404



def update_player_wins(request):
    if request.method == 'POST':
        # Get the winner's username from the submitted form data
        winner_username = request.POST.get('winner_username')

        # Query the Player model to find the player with the winner's username
        try:
            winner_player = Player.objects.get(username=winner_username)
        except Player.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Player not found.'}, status=404)

        # Increment the wins column for the winner player
        winner_player.wins += 1
        winner_player.save()

        # Optionally, you can return a success response
        return JsonResponse({'status': 'success', 'message': "Player's wins updated successfully."})

    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed.'}, status=405)




def gameboard_view(request, player1_id, player2_id):
    # Retrieve player objects from the database
    player1 = get_object_or_404(Player, id=player1_id)
    player2 = get_object_or_404(Player, id=player2_id)


    # Check if a game exists between these players, if not, create a new game
    game = Game.objects.filter(player1=player1, player2=player2).first()
    if not game:
        game = Game.objects.create(player1=player1, player2=player2, current_player=player1)  # Set player1 as the initial current player

    # Pass player objects and game object to the template context
    return render(request, 'gameboard.html', {'player1': player1, 'player2': player2, 'game': game,'current_player': player1,})



def landing_page(request):
  """Renders the landing page template."""
  return render(request, 'landing.html')





def register(request):
    if request.method == 'POST':
        player1_type = request.POST.get('player1_type')
        player2_type = request.POST.get('player2_type')

        # Handle Player 1 selection
        if player1_type == 'registered':
            player1_username = request.POST.get('player1_username')
            player1 = Player.objects.filter(username=player1_username).first()
            if not player1:
                return JsonResponse({'error':'Selected Player 1 does not exist!'},status=400)
        else:
            player1_username = request.POST.get('player1_new_username')
            if not player1_username:
                return JsonResponse({'error': 'Please enter a username for Player 1!'}, status=400)

            # Check if the username already exists
            if Player.objects.filter(username=player1_username).exists():
                return JsonResponse({'error': 'Username already exists for Player 1!'}, status=400)
            
            player1 = Player.objects.create(username=player1_username)

        # Handle Player 2 selection
        if player2_type == 'registered':
            player2_username = request.POST.get('player2_username')
            player2 = Player.objects.filter(username=player2_username).first()
            if not player2:
                return JsonResponse({'error': 'Selected Player 2 does not exist!'}, status=400)
        else:
            player2_username = request.POST.get('player2_new_username')
            if not player2_username:
                return JsonResponse({'error': 'Please enter a username for Player 2!'}, status=400)
            
            # Check if the username already exists
            if Player.objects.filter(username=player2_username).exists():
                return JsonResponse({'error': 'Username already exists for Player 2!'}, status=400)
            
            player2 = Player.objects.create(username=player2_username)

        # Redirect to game board with player information
        return JsonResponse({'redirect_url': reverse('gameboard_view', kwargs={'player1_id': player1.id, 'player2_id': player2.id})})
    else:
        existing_players = Player.objects.all()
        
        return render(request, 'register.html', {'existing_players': existing_players})


def leaderboard(request):
    # Retrieve all players ordered by wins in descending order
    players = Player.objects.all().order_by('-wins')
    return render(request, 'leaderboard.html', {'players': players})
