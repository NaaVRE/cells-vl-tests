
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--str_nums_new_lines', action='store', type=str, required=True, dest='str_nums_new_lines')


args = arg_parser.parse_args()
print(args)

id = args.id

str_nums_new_lines = json.loads(args.str_nums_new_lines)



assert str_nums_new_lines == [1, 2, 3]

