from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Bet

def index(request):
    bets = Bet.objects.order_by('created_at')
    template = loader.get_template('bets/index.html')
    context = {
        'bets': bets,
    }
    return HttpResponse(template.render(context, request))

def detail(request, bet_id):
    bet = get_object_or_404(Bet, pk=bet_id)
    template = loader.get_template('bets/detail.html')
    context = {
        'bet': bet,
    }
    return HttpResponse(template.render(context, request))

def new(request):
    template = loader.get_template('bets/new.html')
    context = {}
    return HttpResponse(template.render(context, request))

def create(request):
    #description, bettor, opponent, wager, deadline
    #redirect to detail of new bet
