
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




int1 = 1

file_int1 = open("/tmp/int1_" + id + ".json", "w")
file_int1.write(json.dumps(int1))
file_int1.close()
