import json


def check_available_centers(**context):
    with open('centers.json', 'r') as openfile:
        available_centers = json.load(openfile)
        if(len(available_centers) > 0):
            return "send_notification"
    return "send_empty_slots_notification"
