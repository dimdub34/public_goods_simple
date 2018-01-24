from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Contribute(Page):
    form_model = 'player'
    form_fields = ['individual_contribution']


class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        for g in self.subsession.get_groups():
            g.set_payoffs()


class Results(Page):
    pass


class End(Page):
    def vars_for_template(self):
        return {"subsession_payoff": c(self.participant.vars["public_goods_simple__payoff"]).to_real_world_currency(self.session)}


page_sequence = [Contribute, ResultsWaitPage, Results, End]
