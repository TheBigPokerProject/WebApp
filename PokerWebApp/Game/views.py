from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from Game.models import Table
# Create your views here.

table = Table()

def pokergame(request):
    global table
    
    if request.method == "POST":
        data = request.POST
        action = data.get("action")
        if action == "startgame":
            if (table.isGameRunning == False):
                table.start_game()
        elif action == "endgame":
            table.reset_table()
    
    return render(request, 'pokergame.html', table.get_context())
