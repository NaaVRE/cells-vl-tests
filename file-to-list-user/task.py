import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_password = os.getenv('secret_password')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--path', action='store', type=str, required=True, dest='path')

arg_parser.add_argument('--param_with_dash', action='store', type=str, required=True, dest='param_with_dash')

args = arg_parser.parse_args()
print(args)

id = args.id

path = args.path.replace('"','')

param_with_dash = args.param_with_dash.replace('"','')

conf_data_folder = conf_data_folder = os.path.join('/tmp', 'data')
conf_user_folder = conf_user_folder = '/home/jovyan/Cloud Storage/naa-vre-user-data/'

print(conf_data_folder)
print(conf_user_folder)
print(param_with_dash)
print(secret_password)

lines = []
if not secret_password:
    raise ValueError('secret_password is empty.') 
if not conf_data_folder:
    raise ValueError('conf_data_folder is empty.') 
if not conf_user_folder:
    raise ValueError('conf_user_folder is empty.') 
if not param_with_dash:
    raise ValueError('param_with_dash is empty.')
if not secret_password:
    raise ValueError('secret_password is empty.')
with open(path) as file:
    while line := file.readline():
        lines.append(line.rstrip())

file_lines = open("/tmp/lines_" + id + ".json", "w")
file_lines.write(json.dumps(lines))
file_lines.close()
