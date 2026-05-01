import json

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




data = {"task": "Write Python", "number": 1, "skills": ["python", "sql"]}

json_str = json.dumps(data)

print(json_str)

file_json_str = open("/tmp/json_str_" + id + ".json", "w")
file_json_str.write(json.dumps(json_str))
file_json_str.close()
