# dags/utils/mongo_utils.py

from pymongo import MongoClient

def get_mongo_client():
    """Returns a MongoClient instance connected to local MongoDB (host.docker.internal)"""
    return MongoClient("host.docker.internal", 27017)

def get_database(db_name="ETL_AIRFLOW_PROJECT"):
    """Returns the MongoDB database object"""
    client = get_mongo_client()
    return client[db_name]