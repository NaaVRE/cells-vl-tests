import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--data_folder', action='store', type=str, required=True, dest='data_folder')


args = arg_parser.parse_args()
print(args)

id = args.id

data_folder = args.data_folder.replace('"','')



file_path = os.path.join(data_folder, 'file.txt')

with open(file_path, "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.\n")
    f.write("Third line.\n")

file_file_path = open("/tmp/file_path_" + id + ".json", "w")
file_file_path.write(json.dumps(file_path))
file_file_path.close()
