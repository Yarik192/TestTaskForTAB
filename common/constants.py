import os

from dotenv import load_dotenv


DEFAULT_BODY = {
    "range": {
        "timezone": "Europe/Istanbul",
    },
    "limit": 1
}

BOGDAN_BODY = {
    "range": {
        "timezone": "Europe/Istanbul",
    },
    "limit": 1,
    "filters": [
        {
            "name": "sub_id_6",
            "operator": "EQUALS",
            "expression": "bogdan"
        }
    ]
}

load_dotenv()  # Загружаем данные из файла .env

# Берём данные из файла .env

API_KEY = os.getenv("API_KEY")
CLICKS_URL = os.getenv("CLICK_URL")
CONVERSION_URL = os.getenv("CONVERSION_URL")
