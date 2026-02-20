
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--names', action='store', type=str, required=True, dest='names')


args = arg_parser.parse_args()
print(args)

id = args.id

names = json.loads(args.names)



new_names = []
for name in names:
    print(f"Hello, {name}!")
    new_names.append(f"Hello, {name}!")

file_new_names = open("/tmp/new_names_" + id + ".json", "w")
file_new_names.write(json.dumps(new_names))
file_new_names.close()
