import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




 

folder = '/home/jovyan/Cloud Storage/naa-vre-user-data'
filename = 'file.txt'

if (os.path.exists(folder)):
    print('folder: ' + folder + ' exists')

path = os.path.join(folder, filename)

with open(path, "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.\n")

file_path = open("/tmp/path_" + id + ".json", "w")
file_path.write(json.dumps(path))
file_path.close()
