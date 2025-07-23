from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from ingestion_weather import ingest_weather
from ingestion_quakes import ingest_quakes
from ingestion_events import ingest_events
from transform_all import transform_all
from load_mongo import load_to_mongo  # 🆕

default_args = {
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='etl_natural_events_pipeline',
    default_args=default_args,
    description='Batch ETL: Weather, Earthquakes, Natural Events → MongoDB',
    schedule_interval='@daily',
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='ingest_weather',
        python_callable=ingest_weather
    )

    t2 = PythonOperator(
        task_id='ingest_quakes',
        python_callable=ingest_quakes
    )

    t3 = PythonOperator(
        task_id='ingest_events',
        python_callable=ingest_events
    )

    t4 = PythonOperator(
        task_id='transform_all',
        python_callable=transform_all
    )

    t5 = PythonOperator(
        task_id='load_to_mongo',
        python_callable=load_to_mongo
    )

    [t1, t2, t3] >> t4 >> t5