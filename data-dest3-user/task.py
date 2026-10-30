import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--var', action='store', type=int, required=True, dest='var')

arg_parser.add_argument('--var2', action='store', type=int, required=True, dest='var2')


args = arg_parser.parse_args()
print(args)

id = args.id

var = args.var
var2 = args.var2



if var !=1:
    os._exit(-1)

if var2 !=1:
    os._exit(-1)

