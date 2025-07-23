# dags/ingestion_quakes.py

import requests
from pymongo import MongoClient
from datetime import datetime

def ingest_quakes(ti=None):
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        ti.xcom_push(key="quakes_raw", value=data)

        client = MongoClient("host.docker.internal", 27017)
        db = client["ETL_AIRFLOW_PROJECT"]
        collection = db["raw_quakes"]

        doc = {
            "source": "usgs",
            "fetched_at": datetime.utcnow().isoformat(),
            "data": data
        }

        collection.insert_one(doc)

    except Exception as e:
        print(f"⚠️ Error in ingest_quakes: {e}")
        ti.xcom_push(key="quakes_raw", value={})