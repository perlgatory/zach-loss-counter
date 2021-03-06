from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

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
    try:
        bet = Bet.objects.create(
            description=request.POST['description'],
            bettor=request.POST['bettor'],
            opponent=request.POST['opponent'],
            wager=request.POST['wager'],
            deadline=request.POST['deadline']
        )
        return HttpResponseRedirect(reverse('detail', args=(bet.id,)))

    except KeyError as error:
        return HttpResponse("There was an issue with {}.".format(error))
