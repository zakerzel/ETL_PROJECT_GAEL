# dags/ingestion_events.py

import requests
from pymongo import MongoClient
from datetime import datetime

def ingest_events(ti=None):
    url = "https://eonet.gsfc.nasa.gov/api/v3/events"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        ti.xcom_push(key="events_raw", value=data)

        client = MongoClient("host.docker.internal", 27017)
        db = client["ETL_AIRFLOW_PROJECT"]
        collection = db["raw_events"]

        doc = {
            "source": "nasa-eonet",
            "fetched_at": datetime.utcnow().isoformat(),
            "data": data
        }

        collection.insert_one(doc)

    except Exception as e:
        print(f"⚠️ Error in ingest_events: {e}")
        ti.xcom_push(key="events_raw", value={})