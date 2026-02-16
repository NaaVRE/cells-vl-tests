import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_password = os.getenv('secret_password')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_with_dash', action='store', type=str, required=True, dest='param_with_dash')

args = arg_parser.parse_args()
print(args)

id = args.id


param_with_dash = args.param_with_dash.replace('"','')

conf_data_folder = conf_data_folder = os.path.join('/tmp', 'data')
conf_user_folder = conf_user_folder = '/home/jovyan/Cloud Storage/naa-vre-user-data/'

print(conf_data_folder)
print(conf_user_folder)
print(param_with_dash)
print(secret_password)

