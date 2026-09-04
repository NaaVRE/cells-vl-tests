
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




secret_test_1 = 'secret'
test_value_1 = [1.2]

file_test_value_1 = open("/tmp/test_value_1_" + id + ".json", "w")
file_test_value_1.write(json.dumps(test_value_1))
file_test_value_1.close()
