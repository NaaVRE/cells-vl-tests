
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--fdo_output', action='store', type=str, required=True, dest='fdo_output')

arg_parser.add_argument('--test_value_1', action='store', type=str, required=True, dest='test_value_1')


args = arg_parser.parse_args()
print(args)

id = args.id

fdo_output = args.fdo_output.replace('"','')
test_value_1 = json.loads(args.test_value_1)



print(test_value_1)
print(fdo_output)

