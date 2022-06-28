
from datetime import date, datetime
import enum
import json
import os
import threading
import time

import holidays

import services
from flask import request
from flask_restx import Namespace, Resource, fields


# Namespace
request_rules_namespace = Namespace(
    'Rules', description="Service to get rules data.")

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]
NAO_HA_EXPEDIENTE = [
    '04-17',
    '05-01',
    '12-24',
    '12-25',
    '12-31'
]
EXPEDIENTE_REDUZIDO = [
    '04-17',
    '05-01',
    '12-24',
    '12-25',
    '12-31'
]
EXPEDIENTE_NORMAL = [
    '03-02'
]

class Signal(enum.Enum):
    reduced_working_hours = "8h as 14h"
    There_is_no_service = "Não há atendimento online"
    normal = "normal"
    date_not_registered = "Data não cadastrada"


@request_rules_namespace.route('/<ano>/')
class RulesRequest(Resource):

    def get(self, ano):
        holidays_poa = []
        for day, description in sorted(holidays.Brazil(years=int(ano), state='RS').items()):
            holidays_poa.append(self.create_object(day, description))

        holidays_poa.append(self.create_object( str(ano) + '-02-02', 'Nossa Sr.a Navegantes'))
        holidays_poa.append(self.create_object( str(ano) + '-12-24', 'Véspera de Natal (ponto facultativo após 14h)'))
        holidays_poa.append(self.create_object( str(ano) + '-12-31', 'Véspera do Ano Novo 2023 (ponto facultativo após 14h)'))

        holidays_poa.sort(key=self.extract_time, reverse=False)
        #print(holidays_poa)
        return holidays_poa, 200

    def office_hour(self, month_and_day):
        if month_and_day in NAO_HA_EXPEDIENTE:
            return Signal.There_is_no_service.value
        elif month_and_day in EXPEDIENTE_REDUZIDO:
            return Signal.reduced_working_hours.value
        elif month_and_day in EXPEDIENTE_NORMAL:
            return Signal.normal.value
        return Signal.date_not_registered.value

    def create_object(self, day, description):
        holiday = {}
        data_split = str(day).split('-')
        holiday["dia"] = str(day)
        holiday["descrição"] = description
        holiday["expediente"] = self.office_hour(str(day)[5:10])
        holiday["dia da semana"] = DIAS[date(year=int(data_split[0]), month=int(data_split[1]), day=int(data_split[2])).weekday()]
        return holiday

    def extract_time(self, json):
        try:
            date = datetime.strptime(json['dia'], '%Y-%m-%d').date()
            return date
        except KeyError:
            return 0

       