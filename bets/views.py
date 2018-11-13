from django.http import HttpResponse
from django.template import loader

from .models import Bet

def index(request):
    bets = Bet.objects.order_by('created_at')
    template = loader.get_template('bets/index.html')
    context = {
        'bets': bets,
    }
    return HttpResponse(template.render(context, request))

def detail(request, bet_id):
    return HttpResponse("You're looking at the details of bet {}".format(bet_id))
