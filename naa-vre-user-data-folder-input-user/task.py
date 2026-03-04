import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




data_folder = os.path.join('/home', 'jovyan','Cloud Storage','naa-vre-user-data')
os.makedirs(data_folder, exist_ok=True)

file_data_folder = open("/tmp/data_folder_" + id + ".json", "w")
file_data_folder.write(json.dumps(data_folder))
file_data_folder.close()
