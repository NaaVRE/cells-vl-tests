
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--lines', action='store', type=str, required=True, dest='lines')


args = arg_parser.parse_args()
print(args)

id = args.id

lines = json.loads(args.lines)



new_lines = []
for line in lines:
    new_lines.append(line+'new')

file_new_lines = open("/tmp/new_lines_" + id + ".json", "w")
file_new_lines.write(json.dumps(new_lines))
file_new_lines.close()
