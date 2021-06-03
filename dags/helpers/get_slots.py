import requests
import json
from datetime import date


def format_center(center):
    center_details = center
    sessions = []
    if ("sessions" in center_details.keys()):
        sessions = center_details["sessions"]
        center_details.pop("sessions")

    return {"center_details": center_details, "sessions": sessions}


def get_slots(**kwargs):
    min_age_limit = kwargs["min_age"]

    available_centers = []

    today = date.today()
    today = today.strftime("%d-%m-%Y")
    filters = {
        "district_id": kwargs["district_id"],
        "date": "23-05-2021",
    }
    request_headers = {
        "accept": "application/json",
        "Accept-Language": "hi_IN",
        'User-Agent': 'ghost',
    }
    response = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict", params=filters, headers=request_headers)

    centers = response.json()['centers']

    for center in centers:
        center_details = center
        sessions = []
        for session in center_details['sessions']:
            if session["min_age_limit"] == min_age_limit:
                sessions.append(session)
        if len(sessions):
            center_details.pop("sessions")
            available_centers.append({
                "center_details": center_details,
                "sessions": sessions
            })

    with open("centers.json", "w") as outfile:
        json.dump(available_centers, outfile)


# get_slots()
