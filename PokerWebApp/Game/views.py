from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from Game.models import Table
# Create your views here.

table = Table()

class AjaxHandlerView(View):

    def get(self, request):
        global table
        action = request.GET.get('action')
        table = Table()

        print(table.get_context())
        return render(request, 'home.html', table.get_context())

    def post(self, request):
        global table
        action = request.POST.get('action')

        if action == 'Start':
            if (table.isGameRunning == False):
                table.start_game()
        else:
            pass

        return render(request, 'home.html', table.get_context())