
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--naa_vre_user_data', action='store', type=str, required=True, dest='naa_vre_user_data')


args = arg_parser.parse_args()
print(args)

id = args.id

naa_vre_user_data = args.naa_vre_user_data.replace('"','')



file = open(naa_vre_user_data, 'r')
content = file.read()
print(content)

