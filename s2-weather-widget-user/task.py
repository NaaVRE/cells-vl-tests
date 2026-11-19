import os
from urllib import request
import json

import argparse
import json
import os

def _load_json_args(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def _parse_value(value, field_name, target_type, elem_type=None):
    if target_type is list:
        if isinstance(value, list):
            return value
        elif isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                # the value may be "['list_str', 'space in elem', '3']"
                if value.startswith('[') and value.endswith(']'):
                    value = value[1:-1].strip()  # remove the brackets and trim whitespace
                    if value:
                        return [elem.strip().strip("'").strip('"') for elem in value.split(',')]
                    else:
                        return []
                else:
                    arg_parser.error(field_name + " is not a valid list")

    if target_type is str:
        return value

    if target_type is int:
        return int(value)

    if target_type is float:
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            return float(value)
    arg_parser.error(field_name + " has unsupported target type")

def get_arg_value(name,args,raw_args):
    for arg in raw_args:
        if arg['name'] == name:
            return arg['value']
    arg_parser.error("Argument '" + name + "' not found in JSON args")

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--args_json', action='store', type=str, required=True, dest='args_json')

args = arg_parser.parse_args()

expected_arg_names = set()
expected_arg_names.add('conf_cities')
expected_arg_names.add('conf_local_tmp')
expected_arg_names.add('id')

raw_args = _load_json_args(args.args_json)
for arg in raw_args:
    if 'name' not in arg:
        arg_parser.error("Argument with no name found in JSON args")
    if arg['name'] not in expected_arg_names:
        arg_parser.error("Unexpected argument '" + arg['name'] + "' found in JSON args")
    if not arg['name'].startswith('conf'):
            if 'value' not in arg or arg['value'] is None:
                arg_parser.error("Argument '" + arg['name'] + "' has no value in JSON args")
    if arg['name'].startswith('conf'):
            if 'assignation' not in arg or arg['assignation'] is None:
                arg_parser.error("Argument '" + arg['name'] + "' has no assignation in JSON args")


conf_cities = {'Amsterdam': (52.37, 4.89), 'Paris': (48.85, 2.35), 'Berlin': (52.52, 13.41), 'Rome': (41.9, 12.5), 'Lisbon': (38.72, -9.14)}
conf_local_tmp = '/tmp/data'


arg_value = get_arg_value('id',args,raw_args)
id = _parse_value(arg_value, 'id', str)

def fetch_json(url):
    with request.urlopen(url, timeout=15) as resp:
        return json.loads(resp.read().decode('utf-8'))

def fetch_current(lat, lon):
    url = (
        'https://api.open-meteo.com/v1/forecast'
        f'?latitude={lat}&longitude={lon}'
        '&current=temperature_2m,relative_humidity_2m,wind_speed_10m'
        '&timezone=auto'
        )
    return fetch_json(url)['current']

os.makedirs(conf_local_tmp, exist_ok=True)

tabs_html = []
for city, (lat, lon) in conf_cities.items():
    current = fetch_current(lat, lon)
    tabs_html.append(
        f"<section><h2>{city}</h2>"
        f"<p><b>{current['temperature_2m']} °C</b><br>"
        f"Humidity: {current['relative_humidity_2m']}%<br>"
        f"Wind: {current['wind_speed_10m']} km/h</p></section>"
        )

page = (
    "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'>"
    "<title>City weather</title><style>"
    "body{font-family:sans-serif;display:flex;gap:1rem;flex-wrap:wrap}"
    "section{border:1px solid #ccc;border-radius:8px;padding:1rem}"
    "</style></head><body>" + "".join(tabs_html) + "</body></html>"
    )

widget_html_path = os.path.join(conf_local_tmp, 'weather_widget.html')
with open(widget_html_path, 'w') as f:
    f.write(page)

print(f'Wrote {widget_html_path}')

file_widget_html_path = open("/tmp/widget_html_path_" + id + ".json", "w")
file_widget_html_path.write(json.dumps(widget_html_path))
file_widget_html_path.close()
