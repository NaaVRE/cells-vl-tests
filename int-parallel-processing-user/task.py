
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--list_int_val', action='store', type=str, required=True, dest='list_int_val')


args = arg_parser.parse_args()
print(args)

id = args.id

list_int_val = json.loads(args.list_int_val)



new_list_int_val = []
for int_val in list_int_val:
    new_list_int_val.append(int_val+1)

file_int_val = open("/tmp/int_val_" + id + ".json", "w")
file_int_val.write(json.dumps(int_val))
file_int_val.close()
file_new_list_int_val = open("/tmp/new_list_int_val_" + id + ".json", "w")
file_new_list_int_val.write(json.dumps(new_list_int_val))
file_new_list_int_val.close()
