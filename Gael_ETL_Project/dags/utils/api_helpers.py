# dags/utils/api_helpers.py

import requests

def fetch_json(url, timeout=10):
    """Fetches JSON data from an API and returns the parsed response or None"""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ API call failed: {url} — {e}")
        return None