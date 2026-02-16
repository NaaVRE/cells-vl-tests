
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_password = os.getenv('secret_password')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--path', action='store', type=str, required=True, dest='path')


args = arg_parser.parse_args()
print(args)

id = args.id

path = args.path.replace('"','')



lines = []
print(secret_password)
with open(path) as file:
    while line := file.readline():
        lines.append(line.rstrip())

file_lines = open("/tmp/lines_" + id + ".json", "w")
file_lines.write(json.dumps(lines))
file_lines.close()
