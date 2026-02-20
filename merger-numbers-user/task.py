
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--new_numbers', action='store', type=str, required=True, dest='new_numbers')


args = arg_parser.parse_args()
print(args)

id = args.id

new_numbers = json.loads(args.new_numbers)



print(new_numbers)

