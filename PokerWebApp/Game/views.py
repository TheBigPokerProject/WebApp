from django.http import HttpResponse
from django.shortcuts import render

from Game.models import Table
# Create your views here.

table = Table()

def home(request):
    table = Table()
    return render(request, 'home.html', table.get_context())

def start_game(request):
    if (table.isGameRunning == False):
        table.start_game()
    return render(request, 'home.html', table.get_context())