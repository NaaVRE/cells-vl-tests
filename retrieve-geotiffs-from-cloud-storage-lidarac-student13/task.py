from pathlib import Path
import shutil

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_earlier_geotiff_file', action='store', type=str, required=True, dest='param_earlier_geotiff_file')
arg_parser.add_argument('--param_geotiff_folder', action='store', type=str, required=True, dest='param_geotiff_folder')
arg_parser.add_argument('--param_later_geotiff_file', action='store', type=str, required=True, dest='param_later_geotiff_file')
arg_parser.add_argument('--param_use_own_data', action='store', type=int, required=True, dest='param_use_own_data')

args = arg_parser.parse_args()
print(args)

id = args.id


param_earlier_geotiff_file = args.param_earlier_geotiff_file.replace('"','')
param_geotiff_folder = args.param_geotiff_folder.replace('"','')
param_later_geotiff_file = args.param_later_geotiff_file.replace('"','')
param_use_own_data = args.param_use_own_data

conf_local_path_geotiff = conf_local_path_geotiff = str(Path('/tmp/data') / param_geotiff_folder)
conf_cloud_storage = conf_cloud_storage = '/home/jovyan/Cloud Storage/'
conf_user_bucket = conf_user_bucket = 'naa-vre-user-data/'
conf_public_bucket = conf_public_bucket = 'naa-vre-public/'
conf_laserfarm_workshop = conf_laserfarm_workshop = 'vl-laserfarm/Workshop/'

def get_file_from_local_cloud_storage(filename: str) -> str:
    cloud_file_path = Path(directory_to_retrieve) / filename
    local_file_path = Path(conf_local_path_geotiff) / filename
    print(f'Downloading{cloud_file_path} to {local_file_path}')
    shutil.copy(cloud_file_path, local_file_path)
    return str(local_file_path)

Path(conf_local_path_geotiff).mkdir(parents=True, exist_ok=True)

if param_use_own_data:
    directory_to_retrieve = str(Path(conf_cloud_storage) / conf_user_bucket / param_geotiff_folder)
else:
    directory_to_retrieve = str(Path(conf_cloud_storage) / conf_public_bucket / conf_laserfarm_workshop / param_geotiff_folder)

earlier_geotiff_file = get_file_from_local_cloud_storage(param_earlier_geotiff_file)
later_geotiff_file = get_file_from_local_cloud_storage(param_later_geotiff_file)

file_earlier_geotiff_file = open("/tmp/earlier_geotiff_file_" + id + ".json", "w")
file_earlier_geotiff_file.write(json.dumps(earlier_geotiff_file))
file_earlier_geotiff_file.close()
file_later_geotiff_file = open("/tmp/later_geotiff_file_" + id + ".json", "w")
file_later_geotiff_file.write(json.dumps(later_geotiff_file))
file_later_geotiff_file.close()
