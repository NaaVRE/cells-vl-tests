
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--path', action='store', type=str, required=True, dest='path')


args = arg_parser.parse_args()
print(args)

id = args.id

path = args.path.replace('"','')



with open(path, "r", encoding="utf-8") as f:
    print(f.read())

