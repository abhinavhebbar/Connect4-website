"""
URL configuration for connect4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import gameboard_view,update_player_wins,landing_page,register,leaderboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('gameboard_view/<int:player1_id>/<int:player2_id>/', gameboard_view, name='gameboard_view'),
    path('update_player_wins/', update_player_wins, name='update_player_wins'),
    path('register/', register, name='register'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    


]
