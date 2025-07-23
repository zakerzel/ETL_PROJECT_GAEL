# dags/ingestion_weather.py

import requests
from pymongo import MongoClient
from datetime import datetime

def ingest_weather(ti=None):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=21.0&longitude=-89.625"
        "&current=temperature_2m,relative_humidity_2m,precipitation"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        ti.xcom_push(key="weather_raw", value=data)

        client = MongoClient("host.docker.internal", 27017)
        db = client["ETL_AIRFLOW_PROJECT"]
        collection = db["raw_weather"]

        doc = {
            "source": "open-meteo",
            "fetched_at": datetime.utcnow().isoformat(),
            "data": data
        }

        collection.insert_one(doc)

    except Exception as e:
        print(f"⚠️ Error in ingest_weather: {e}")
        ti.xcom_push(key="weather_raw", value={})