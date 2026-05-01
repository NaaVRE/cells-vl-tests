import json

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--json_str', action='store', type=str, required=True, dest='json_str')


args = arg_parser.parse_args()
print(args)

id = args.id

json_str = args.json_str.replace('"','')



print(json_str)
deserialized_data = json.loads(json_str)

print(deserialized_data)

