from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Dimitri DUBOIS'

doc = """
Simple public goods game played in one-shot
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_simple'
    players_per_group = 2
    num_rounds = 1
    endowment = 20
    mpcr = 0.6


class Subsession(BaseSubsession):
    treatment = models.IntegerField()

    def creating_session(self):
        self.treatment = self.session.config["treatment"]


class Group(BaseGroup):
    group_contribution = models.IntegerField()

    def set_payoffs(self):
        self.group_contribution = sum([p.individual_contribution for p in self.get_players()])
        payoff_coll_account = float("{:.2f}".format(self.group_contribution * Constants.mpcr))
        for p in self.get_players():
            p.payoff_collective_account = payoff_coll_account
            p.payoff_individual_account = Constants.endowment - p.individual_contribution
            p.payoff = p.payoff_individual_account + p.payoff_collective_account
            p.participant.vars["public_goods_simple__payoff"] = p.payoff


class Player(BasePlayer):
    individual_contribution = models.IntegerField(min=0, max=Constants.endowment)
    payoff_collective_account = models.FloatField()
    payoff_individual_account = models.FloatField()
