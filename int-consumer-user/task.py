
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--int1', action='store', type=int, required=True, dest='int1')


args = arg_parser.parse_args()
print(args)

id = args.id

int1 = args.int1



print(int1)

