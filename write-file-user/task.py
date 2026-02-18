
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--file_path', action='store', type=str, required=True, dest='file_path')


args = arg_parser.parse_args()
print(args)

id = args.id

file_path = args.file_path.replace('"','')



lines = []
with open(file_path) as file:
    while line := file.readline():
        lines.append(line.rstrip())

file_lines = open("/tmp/lines_" + id + ".json", "w")
file_lines.write(json.dumps(lines))
file_lines.close()
