
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--int2', action='store', type=int, required=True, dest='int2')


args = arg_parser.parse_args()
print(args)

id = args.id

int2 = args.int2



print(int2)

