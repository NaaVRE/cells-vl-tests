
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--list_nums', action='store', type=str, required=True, dest='list_nums')


args = arg_parser.parse_args()
print(args)

id = args.id

list_nums = json.loads(args.list_nums)



list_nums_new_lines = []
for line in list_nums:
    print(line)
    list_nums_new_lines.append(line)

file_list_nums_new_lines = open("/tmp/list_nums_new_lines_" + id + ".json", "w")
file_list_nums_new_lines.write(json.dumps(list_nums_new_lines))
file_list_nums_new_lines.close()
