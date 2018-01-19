# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('otree', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('group_contribution', otree.db.models.IntegerField(null=True)),
                ('session', models.ForeignKey(to='otree.Session', related_name='public_goods_simple_group')),
            ],
            options={
                'db_table': 'public_goods_simple_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(null=True, default=0)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('individual_contribution', otree.db.models.IntegerField(null=True)),
                ('payoff_collective_account', otree.db.models.FloatField(null=True)),
                ('payoff_individual_account', otree.db.models.FloatField(null=True)),
                ('group', models.ForeignKey(to='public_goods_simple.Group', null=True)),
                ('participant', models.ForeignKey(to='otree.Participant', related_name='public_goods_simple_player')),
                ('session', models.ForeignKey(to='otree.Session', related_name='public_goods_simple_player')),
            ],
            options={
                'db_table': 'public_goods_simple_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(to='otree.Session', null=True, related_name='public_goods_simple_subsession')),
            ],
            options={
                'db_table': 'public_goods_simple_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(to='public_goods_simple.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(to='public_goods_simple.Subsession'),
        ),
    ]
