
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--str_list_nums', action='store', type=str, required=True, dest='str_list_nums')


args = arg_parser.parse_args()
print(args)

id = args.id

str_list_nums = json.loads(args.str_list_nums)



str_nums_new_lines = []
for line in str_list_nums:
    print(line)
    str_nums_new_lines.append(line)

file_str_nums_new_lines = open("/tmp/str_nums_new_lines_" + id + ".json", "w")
file_str_nums_new_lines.write(json.dumps(str_nums_new_lines))
file_str_nums_new_lines.close()
