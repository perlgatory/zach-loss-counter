from django.db import models
from .enums import *
from enumchoicefield import ChoiceEnum, EnumChoiceField

# Create your models here.

class Bet(models.Model):
    description = models.TextField()
    wager =  models.TextField()
    bettor = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    deadline = models.DateTimeField('end date')
    created_at = models.DateTimeField('bet made date', auto_now_add=True)
    outcome = EnumChoiceField(BetResultChoice, blank=True, null=True)
    state = EnumChoiceField(BetStateChoice, default=BetStateChoice.O)

    def __str__(self):
        return "Description: {}, Bettor: {}, Opponent: {}, Deadline: {}, Outcome: {}".format(self.description, self.bettor, self.opponent, self.deadline, self.outcome)
