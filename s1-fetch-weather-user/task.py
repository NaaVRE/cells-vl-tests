import os
import json
from urllib import request

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
expected_arg_names.add('param_city')
expected_arg_names.add('param_forecast_hours')
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

arg_name = 'param_city'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
param_city = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'param_forecast_hours'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
param_forecast_hours = _parse_value(arg_value, arg_name, arg_type)

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

def fetch_hourly(lat, lon, hours):
    url = (
        'https://api.open-meteo.com/v1/forecast'
        f'?latitude={lat}&longitude={lon}'
        '&hourly=temperature_2m&forecast_days=2&timezone=auto'
        )
    return fetch_json(url)['hourly']['temperature_2m'][:hours]

os.makedirs(conf_local_tmp, exist_ok=True)

lat, lon = conf_cities[param_city]
hourly_temps = fetch_hourly(lat, lon, int(param_forecast_hours))
forecast_path = os.path.join(conf_local_tmp, 'forecast.csv')
with open(forecast_path, 'w', encoding='utf-8') as f:
    f.write('hour,temperature_c\n')
    for i, t in enumerate(hourly_temps):
        f.write(f'{i},{t}\n')
print(f'Wrote {forecast_path} ({len(hourly_temps)} rows)')

features = []
for city, (city_lat, city_lon) in conf_cities.items():
    current = fetch_current(city_lat, city_lon)
    features.append({
        'type': 'Feature',
        'properties': {
            'name': city,
            'temperature_c': current['temperature_2m'],
            'humidity_pct': current['relative_humidity_2m'],
            'wind_speed_kmh': current['wind_speed_10m'],
            },
        'geometry': {'type': 'Point', 'coordinates': [city_lon, city_lat]},
        })

cities_geojson_path = os.path.join(conf_local_tmp, 'cities.geojson')
with open(cities_geojson_path, 'w', encoding='utf-8') as f:
    json.dump({'type': 'FeatureCollection', 'features': features}, f)
print(f'Wrote {cities_geojson_path} ({len(features)} features)')

summary_path = os.path.join(conf_local_tmp, 'summary.csv')
with open(summary_path, 'w', encoding='utf-8') as f:
    f.write('city,temperature_c,humidity_pct,wind_speed_kmh\n')
    for feat in features:
        p = feat['properties']
        f.write(f"{p['name']},{p['temperature_c']},{p['humidity_pct']},{p['wind_speed_kmh']}\n")
print(f'Wrote {summary_path}')

file_forecast_path = open("/tmp/forecast_path_" + id + ".json", "w")
file_forecast_path.write(json.dumps(forecast_path))
file_forecast_path.close()
file_cities_geojson_path = open("/tmp/cities_geojson_path_" + id + ".json", "w")
file_cities_geojson_path.write(json.dumps(cities_geojson_path))
file_cities_geojson_path.close()
file_summary_path = open("/tmp/summary_path_" + id + ".json", "w")
file_summary_path.write(json.dumps(summary_path))
file_summary_path.close()
