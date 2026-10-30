
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--list_nums_new_lines', action='store', type=str, required=True, dest='list_nums_new_lines')


args = arg_parser.parse_args()
print(args)

id = args.id

list_nums_new_lines = json.loads(args.list_nums_new_lines)



assert list_nums_new_lines == [1, 2, 3]

