# dags/transform_all.py

from datetime import datetime
from utils.transform_helpers import (
    classify_temperature,
    classify_magnitude,
    is_severe_event
)

def transform_all(ti=None):
    # 1️⃣ Weather transformation
    raw_weather = ti.xcom_pull(key="weather_raw", task_ids="ingest_weather")
    if raw_weather and "current" in raw_weather:
        current = raw_weather["current"]
        temp = current.get("temperature_2m")
        doc = {
            "timestamp": current.get("time"),
            "temperature_c": temp,
            "humidity_percent": current.get("relative_humidity_2m"),
            "precipitation_mm": current.get("precipitation"),
            "temperature_class": classify_temperature(temp),
            "is_extreme_temp": temp > 35 if temp else False,
            "is_rain": current.get("precipitation", 0) > 0,
            "transformed_at": datetime.utcnow().isoformat()
        }
        ti.xcom_push(key="processed_weather", value=doc)

    # 2️⃣ Earthquake transformation
    raw_quakes = ti.xcom_pull(key="quakes_raw", task_ids="ingest_quakes")
    transformed_quakes = []
    if raw_quakes and "features" in raw_quakes:
        for quake in raw_quakes["features"]:
            prop = quake.get("properties", {})
            coords = quake.get("geometry", {}).get("coordinates", [])
            if prop and coords:
                mag = prop.get("mag")
                transformed_quakes.append({
                    "magnitude": mag,
                    "magnitude_class": classify_magnitude(mag),
                    "location": prop.get("place"),
                    "timestamp": datetime.utcfromtimestamp(prop["time"] / 1000).isoformat(),
                    "depth_km": coords[2] if len(coords) == 3 else None,
                    "longitude": coords[0],
                    "latitude": coords[1],
                    "is_strong": mag >= 4.5 if mag else False,
                    "transformed_at": datetime.utcnow().isoformat()
                })
        ti.xcom_push(key="processed_quakes", value=transformed_quakes)

    # 3️⃣ Natural Events transformation
    raw_events = ti.xcom_pull(key="events_raw", task_ids="ingest_events")
    transformed_events = []
    if raw_events and "events" in raw_events:
        for event in raw_events["events"]:
            geo = event.get("geometry", [])
            if geo:
                last_point = geo[-1]
                cat = event.get("categories", [{}])[0].get("title", "Unknown")
                transformed_events.append({
                    "event_id": event.get("id"),
                    "title": event.get("title"),
                    "category": cat,
                    "date": last_point.get("date"),
                    "longitude": last_point.get("coordinates", [None])[0],
                    "latitude": last_point.get("coordinates", [None, None])[1],
                    "is_severe": is_severe_event(cat),
                    "transformed_at": datetime.utcnow().isoformat()
                })
        ti.xcom_push(key="processed_events", value=transformed_events)