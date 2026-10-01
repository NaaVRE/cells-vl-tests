
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--a_list', action='store', type=str, required=True, dest='a_list')


args = arg_parser.parse_args()
print(args)

id = args.id

a_list = json.loads(args.a_list)



new_numbers = []
for num in a_list:
    num+=1
    new_numbers.append(num)

    
    

