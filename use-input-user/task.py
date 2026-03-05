
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--var', action='store', type=int, required=True, dest='var')


args = arg_parser.parse_args()
print(args)

id = args.id

var = args.var



print(var)

