# 🌍 ETL Airflow Project — Natural Events Monitoring

This project implements a **batch ETL pipeline** using **Apache Airflow**, **MongoDB**, and **Streamlit**, designed to ingest and visualize real-world environmental data.

## 🧠 Objective

To build a fully dockerized data pipeline that:

- Ingests data from **three public APIs**
- Transforms and enriches the data
- Stores raw and processed versions in MongoDB
- Displays the processed results through an interactive **Streamlit dashboard**

---

## 🌐 Public APIs Used

| Source | API | Link |
|--------|-----|------|
| 🌤️ Weather | Open-Meteo | [open-meteo.com](https://open-meteo.com/en/docs) |
| 🌎 Earthquakes | USGS Earthquake API | [earthquake.usgs.gov](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) |
| 🔥 Natural Events | NASA EONET API | [eonet.gsfc.nasa.gov](https://eonet.gsfc.nasa.gov/docs/v3) |

---

## 🗃️ MongoDB Collections

| Type | Collection | Purpose |
|------|------------|---------|
| Raw  | `raw_weather`<br>`raw_quakes`<br>`raw_events` | Stores unprocessed API data |
| Processed | `processed_weather`<br>`processed_quakes`<br>`processed_events` | Cleaned, enriched data for dashboard |

---

## ⚙️ How to Run

### 1. Clone the project

```bash
git clone https://github.com/youruser/your-etl-project.git
cd your-etl-project
2. Start all services with Docker
bash
Copiar
Editar
docker-compose up --build
This starts:

Airflow (webserver + scheduler)

PostgreSQL (metadata)

MongoDB (data storage)

Streamlit dashboard

🛠️ How to Use
🔄 Run the ETL DAG
Visit Airflow UI at http://localhost:8080

DAG name: etl_natural_events_pipeline

Toggle it on (🟢)

Click "Trigger DAG" to execute manually

📄 Check logs
Go to the DAG > Task Instances

Click any task > "View Log"

📊 Streamlit Dashboard
Visit http://localhost:8501

You can:

View current weather in Mérida, Yucatán

Browse recent earthquakes

Filter natural events by category (e.g., wildfires, volcanoes)

🔁 XCom Usage
Airflow XComs are used to pass data between tasks:

Each ingest_*.py task pushes raw API data to XCom

transform_all.py pulls from XCom, cleans data, and pushes transformed records

load_mongo.py pulls transformed records from XCom and inserts them into MongoDB

📂 Folder Structure
Copiar
Editar
project-root/
├── dags/
│   ├── main_pipeline.py
│   ├── ingestion_weather.py
│   ├── ingestion_quakes.py
│   ├── ingestion_events.py
│   ├── transform_all.py
│   ├── load_mongo.py
│   └── utils/
│       ├── mongo_utils.py
│       ├── api_helpers.py
│       └── transform_helpers.py
│
├── streamlit_app/
│   ├── app.py
│   └── Dockerfile
│
├── docker-compose.yml
├── requirements.txt
└── README.md
✅ Project Checklist
 ETL DAG with 5+ tasks

 3 public APIs

 MongoDB for raw + processed data

 Streamlit dashboard

 Dockerized solution

 XComs between tasks

Developed as part of the Massive Data Management course at Universidad Politécnica de Yucatán.