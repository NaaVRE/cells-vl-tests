import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




folder_path = '/home/jovyan/Cloud Storage/naa-vre-user-data/'
filename = 'file.txt'
path = os.path.join(folder_path, filename)

with open(path, "a", encoding="utf-8") as f:
    f.write("Appended line.\n")

file_path = open("/tmp/path_" + id + ".json", "w")
file_path.write(json.dumps(path))
file_path.close()
