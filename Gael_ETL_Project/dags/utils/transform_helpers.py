# dags/utils/transform_helpers.py

def classify_temperature(temp_c):
    if temp_c is None:
        return "unknown"
    elif temp_c >= 40:
        return "extreme"
    elif temp_c >= 30:
        return "hot"
    elif temp_c >= 20:
        return "warm"
    elif temp_c >= 10:
        return "cool"
    else:
        return "cold"

def classify_magnitude(mag):
    if mag is None:
        return "unknown"
    elif mag >= 6.0:
        return "strong"
    elif mag >= 4.5:
        return "moderate"
    elif mag >= 3.0:
        return "light"
    else:
        return "minor"

def is_severe_event(category):
    return category in ["Volcanoes", "Storms", "Severe Storm"]