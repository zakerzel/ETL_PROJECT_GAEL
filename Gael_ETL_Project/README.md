# 🌍 ETL Airflow Project — Natural Events Monitoring

This project implements a batch ETL pipeline using Apache Airflow, MongoDB, and Streamlit, designed to ingest and visualize real-world environmental data.

---

## 🧠 Objective

To build a fully dockerized data pipeline that:

- Ingests data from three public APIs
- Transforms and enriches the data
- Stores raw and processed versions in MongoDB
- Displays the processed results through an interactive Streamlit dashboard

---

## 🌐 Public APIs Used

| Source         | API Name           | Link                        |
|----------------|--------------------|-----------------------------|
| 🌤️ Weather     | Open-Meteo         | https://open-meteo.com/     |
| 🌎 Earthquakes | USGS Earthquake API| https://earthquake.usgs.gov/|
| 🔥 Natural Events | NASA EONET API | https://eonet.gsfc.nasa.gov/|

---

## ⚙️ How to Run (Step-by-step)

### 1. Clone the repository

git clone https://github.com/zakerzel/ETL_PROJECT_GAEL.git

### 2. Start all services using Docker Compose
docker-compose up --build

This will start:

Airflow (webserver + scheduler)

PostgreSQL (Airflow metadata)

MongoDB (data storage)

Streamlit dashboard

Wait ~30–60 seconds until all services are fully initialized.

### 3. Access the Airflow UI
Open: http://localhost:8080

Login:

Username: admin

Password: admin

📥 Trigger the ETL pipeline
Locate the DAG: etl_natural_events_pipeline

Turn it on (toggle switch 🟢)

Click “Trigger DAG” (lightning icon ⚡)

### 4. Check DAG execution & logs
Click on the DAG name

Go to the Graph View or Tree View

Click on any task (e.g., ingest_weather)

Click “View Log” to see output from each step

### 5. Open the Streamlit Dashboard
Visit: http://localhost:8501

You can:

View current weather in Mérida, Yucatán

Browse recent earthquakes

Filter natural events (e.g., wildfires, volcanoes)

### Developed for
Massive Data Management course
Universidad Politécnica de Yucatán
Student: Gael Lara Peña
