from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class InstructionsRead(Page):
    def is_displayed(self):
        return self.round_number == 1


class Contribute(Page):
    form_model = 'player'
    form_fields = ['individual_contribution']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


class End(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    # def vars_for_template(self):
    #     return {"final_payoff": self.participant.payoff_plus_participation_fee()}


page_sequence = [
    Instructions,
    InstructionsRead,
    Contribute,
    ResultsWaitPage,
    Results,
    End
]
