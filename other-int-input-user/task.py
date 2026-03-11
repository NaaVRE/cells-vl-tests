
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




int2 = 2

file_int2 = open("/tmp/int2_" + id + ".json", "w")
file_int2.write(json.dumps(int2))
file_int2.close()
