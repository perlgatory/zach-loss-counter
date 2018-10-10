from django.db import models
from .enums import *

# Create your models here.

class Bet(models.Model):
    description = models.TextField()
    wager =  models.TextField()
    bettor = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    deadline = models.DateTimeField('end date')
    created_at = models.DateTimeField('bet made date', auto_now_add=True)
    outcome = models.CharField(
        choices=[(tag, tag.value) for tag in BetResultChoice], 
        max_length=1,
        blank=True 
    )
    state = models.CharField(
        choices=[(tag, tag.value) for tag in BetStateChoice],
        max_length=1,
        default=BetStateChoice.O
    )
