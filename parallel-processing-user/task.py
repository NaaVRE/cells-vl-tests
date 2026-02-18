
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
    line += '_processed'
    print(line)
    new_lines.append(line)

