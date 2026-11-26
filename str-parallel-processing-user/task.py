
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--str_list', action='store', type=str, required=True, dest='str_list')


args = arg_parser.parse_args()
print(args)

id = args.id

str_list = json.loads(args.str_list)



new_lines = []
for line in str_list:
    line += '_processed'
    print(line)
    new_lines.append(line)

file_new_lines = open("/tmp/new_lines_" + id + ".json", "w")
file_new_lines.write(json.dumps(new_lines))
file_new_lines.close()
