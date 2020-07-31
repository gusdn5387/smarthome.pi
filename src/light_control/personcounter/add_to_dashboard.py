import requests
import json

API_DASHBOARD_HOST = 'http://127.0.0.1'
API_DASHBOARD_PORT = '8000'


def add_ledstatus_to_dashboard(is_on:bool):
    requests.post(f'{API_DASHBOARD_HOST}:{API_DASHBOARD_PORT}/lightcontrol/ledstatus/',
                  json=json.dumps({"is_on": is_on}))
    return True

def add_roomstatus_to_dashboard(people_count:int):
    requests.post(f'{API_DASHBOARD_HOST}:{API_DASHBOARD_PORT}/lightcontrol/roomstatus/',
                  json=json.dumps({"people_count": people_count}))
    return True
