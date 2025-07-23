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
cd ETL_PROJECT_GAEL/Gael_ETL_Project

### 2. Start all services using Docker Compose
docker-compose up --build

This will start:

Airflow (webserver + scheduler)

PostgreSQL (Airflow metadata)

MongoDB (data storage)

Streamlit dashboard

Wait ~30–60 seconds until all services are fully initialized.

### 🔐 Step 3: Create Airflow user (in a second terminal)

After running `docker-compose up --build`, open another Git Bash terminal window and run:

docker-compose run --rm webserver airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin

### 4. Access the Airflow UI
Open: http://localhost:8080

Login:

Username: admin

Password: admin

📥 Trigger the ETL pipeline
Locate the DAG: etl_natural_events_pipeline

Turn it on (toggle switch 🟢)

Click “Trigger DAG” (lightning icon ⚡)

### 5. Check DAG execution & logs
Click on the DAG name

Go to the Graph View or Tree View

Click on any task (e.g., ingest_weather)

Click “View Log” to see output from each step

### 6. Open the Streamlit Dashboard
Visit: http://localhost:8501

You can:

View current weather in Mérida, Yucatán

Browse recent earthquakes

Filter natural events (e.g., wildfires, volcanoes)

### 📂 Project Structure
Gael_ETL_Project/
├── dags/
│   ├── ingestion_weather.py
│   ├── ingestion_quakes.py
│   ├── ingestion_events.py
│   ├── transform_all.py
│   ├── load_mongo.py
│   ├── main_pipeline.py
│   └── utils/
│       ├── api_helpers.py
│       ├── mongo_utils.py
│       └── transform_helpers.py
│
├── streamlit_app/
│   ├── app.py
│   └── Dockerfile
│
├── docker-compose.yml
├── requirements.txt
└── README.md

### Developed for
Massive Data Management course
Universidad Politécnica de Yucatán
Student: Gael Lara Peña
