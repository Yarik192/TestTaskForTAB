import copy
import json

import requests

from common.constants import DEFAULT_BODY, BOGDAN_BODY, API_KEY, CLICKS_URL, CONVERSION_URL


def get_body(name: str, date_from: str, date_to: str) -> dict:
    """
    Формируем запрос из полученных данных.
    :param name:
    :param date_from:
    :param date_to:
    :return body:
    """
    body: dict
    if name == "bogdan":
        body = copy.deepcopy(BOGDAN_BODY)  # Глубокое копирование для неизменяемости исходного объекта
    else:
        body = copy.deepcopy(DEFAULT_BODY.copy())
    if date_from:
        body["range"]["from"] = date_from
    if date_to:
        body["range"]["to"] = date_to
    if not date_from and not date_to:
        body["range"]["interval"] = "today"
    return body


def get_clicks(name: str, date_from: str, date_to: str) -> int:
    url = CLICKS_URL
    header = {"Api-Key": API_KEY}
    body = get_body(name, date_from, date_to)
    data = requests.post(url, headers=header, data=json.dumps(body))
    return int(json.loads(data.text)["total"])


def get_conversion(name: str, date_from: str, date_to: str) -> int:
    url = CONVERSION_URL
    header = {"Api-Key": API_KEY}
    body = get_body(name, date_from, date_to)
    data = requests.post(url, headers=header, data=json.dumps(body))
    return int(json.loads(data.text)["total"])


def get_data(name: str, date_from: str = False, date_to: str = False) -> dict:
    """
    Получаем данные по тем параметрам которые пришли.
    :param name:
    :param date_from:
    :param date_to:
    :return:
    """
    data = {}
    if name == "bogdan":
        data["clicks"] = get_clicks(name, date_from, date_to)
        data["conversion"] = get_conversion(name, date_from, date_to)
    else:
        data["clicks"] = get_clicks(name, date_from, date_to) - get_clicks("bogdan", date_from, date_to)
        data["conversion"] = get_conversion(name, date_from, date_to) - get_conversion("bogdan", date_from, date_to)

    return data
