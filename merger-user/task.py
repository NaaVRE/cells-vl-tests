
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--new_names', action='store', type=str, required=True, dest='new_names')


args = arg_parser.parse_args()
print(args)

id = args.id

new_names = json.loads(args.new_names)



print(new_names)

