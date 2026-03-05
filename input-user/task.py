
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




var = 1

file_var = open("/tmp/var_" + id + ".json", "w")
file_var.write(json.dumps(var))
file_var.close()
