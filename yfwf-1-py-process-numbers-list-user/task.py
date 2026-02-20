
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--numbers', action='store', type=str, required=True, dest='numbers')


args = arg_parser.parse_args()
print(args)

id = args.id

numbers = json.loads(args.numbers)



new_numbers = []
for number in numbers:
    new_numbers.append(number + 1 )

file_new_numbers = open("/tmp/new_numbers_" + id + ".json", "w")
file_new_numbers.write(json.dumps(new_numbers))
file_new_numbers.close()
