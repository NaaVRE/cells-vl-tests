
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




str_list_nums = ["1","2","3"]

file_str_list_nums = open("/tmp/str_list_nums_" + id + ".json", "w")
file_str_list_nums.write(json.dumps(str_list_nums))
file_str_list_nums.close()
