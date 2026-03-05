
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--now', action='store', type=str, required=True, dest='now')


args = arg_parser.parse_args()
print(args)

id = args.id

now = args.now.replace('"','')



print(now)

