import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--string_val', action='store', type=str, required=True, dest='string_val')


args = arg_parser.parse_args()
print(args)

id = args.id

string_val = args.string_val.replace('"','')


conf_data_folder = conf_data_folder = os.path.join('/tmp', 'data')
conf_user_folder = conf_user_folder = '/home/jovyan/Cloud Storage/naa-vre-user-data/'

os.makedirs(conf_data_folder, exist_ok=True)

file_path = os.path.join(conf_user_folder, string_val)

with open(file_path, "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.\n")
    f.write("Third line.\n")


with open(file_path, "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.\n")
    f.write("Third line.\n")

file_file_path = open("/tmp/file_path_" + id + ".json", "w")
file_file_path.write(json.dumps(file_path))
file_file_path.close()
