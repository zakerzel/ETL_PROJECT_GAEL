# streamlit_app/app.py

import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Conexión a MongoDB
client = MongoClient("host.docker.internal", 27017)
db = client["ETL_AIRFLOW_PROJECT"]

st.set_page_config(page_title="🌍 Natural Events Dashboard", layout="wide")
st.title("🌪️ Natural Events Monitoring Dashboard")

# --- Weather Section ---
st.header("🌤️ Weather in Mérida, Yucatán")
weather_doc = db["processed_weather"].find_one(sort=[("transformed_at", -1)])

if weather_doc:
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature (°C)", f"{weather_doc['temperature_c']}°", weather_doc["temperature_class"])
    col2.metric("Humidity (%)", weather_doc["humidity_percent"])
    col3.metric("Precipitation (mm)", weather_doc["precipitation_mm"])
else:
    st.warning("No weather data available.")

# --- Earthquakes Section ---
st.header("🌎 Earthquakes in the Last 24 Hours")

quakes_cursor = db["processed_quakes"].find().sort("timestamp", -1)
quakes = list(quakes_cursor)
if quakes:
    df_quakes = pd.DataFrame(quakes)
    mag_filter = st.slider("Minimum Magnitude", 0.0, 10.0, 3.5, 0.1)
    df_quakes = df_quakes[df_quakes["magnitude"] >= mag_filter]
    st.dataframe(df_quakes[["timestamp", "location", "magnitude", "magnitude_class", "depth_km"]])
else:
    st.warning("No earthquake data found.")

# --- Natural Events Section ---
st.header("🔥 Natural Events from NASA EONET")

events = list(db["processed_events"].find().sort("date", -1))
if events:
    df_events = pd.DataFrame(events)
    selected_category = st.selectbox("Filter by Category", options=["All"] + sorted(df_events["category"].unique().tolist()))
    if selected_category != "All":
        df_events = df_events[df_events["category"] == selected_category]

    st.dataframe(df_events[["title", "category", "date", "latitude", "longitude", "is_severe"]])
else:
    st.warning("No natural events found.")