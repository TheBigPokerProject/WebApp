from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    context = sampleHandForAllPlayers()
    return render(request, 'home.html', context)

def sampleHandForAllPlayers():
    return {"p1" : "5H,3S", "p2" : "JD,TD", "p3" : "AH,AS", "p4" : "KH,QS", "p5" : "2H,7C", "p6" : "5C,5D", "p7" : "7H,7S", "p8" : "9S,4H"}