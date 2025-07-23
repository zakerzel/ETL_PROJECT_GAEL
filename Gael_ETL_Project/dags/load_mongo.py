# dags/load_mongo.py

from pymongo import MongoClient

def load_to_mongo(ti=None):
    client = MongoClient("host.docker.internal", 27017)
    db = client["ETL_AIRFLOW_PROJECT"]

    # Weather
    weather = ti.xcom_pull(key="processed_weather", task_ids="transform_all")
    if weather:
        db["processed_weather"].insert_one(weather)

    # Quakes
    quakes = ti.xcom_pull(key="processed_quakes", task_ids="transform_all")
    if quakes:
        db["processed_quakes"].insert_many(quakes)

    # Events
    events = ti.xcom_pull(key="processed_events", task_ids="transform_all")
    if events:
        db["processed_events"].insert_many(events)