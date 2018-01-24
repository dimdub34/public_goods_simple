from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
from random import randint


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Contribute, {'individual_contribution': randint(0, Constants.endowment)})
        yield (pages.Results)
        yield Submission(pages.End, check_html=False)

