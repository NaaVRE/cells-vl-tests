import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id



conf_data_folder = conf_data_folder = os.path.join('/tmp', 'data')
conf_user_folder = conf_user_folder = '/home/jovyan/Cloud Storage/naa-vre-user-data/'

os.makedirs(conf_data_folder, exist_ok=True)
filename = 'file.txt'
path = os.path.join(conf_data_folder, filename)

with open(path, "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.\n")
    f.write("Third line.\n")

path = os.path.join(conf_user_folder, filename)

with open(path, "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.\n")
    f.write("Third line.\n")

file_path = open("/tmp/path_" + id + ".json", "w")
file_path.write(json.dumps(path))
file_path.close()
