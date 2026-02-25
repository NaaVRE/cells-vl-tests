
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--list_duble_val', action='store', type=str, required=True, dest='list_duble_val')


args = arg_parser.parse_args()
print(args)

id = args.id

list_duble_val = json.loads(args.list_duble_val)



new_list_duble_val = []
for double_val in list_duble_val:
    new_list_duble_val.append(double_val+1.1)

file_new_list_duble_val = open("/tmp/new_list_duble_val_" + id + ".json", "w")
file_new_list_duble_val.write(json.dumps(new_list_duble_val))
file_new_list_duble_val.close()
