
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--float_type', action='store', type=str, required=True, dest='float_type')

arg_parser.add_argument('--float_val', action='store', type=float, required=True, dest='float_val')

arg_parser.add_argument('--int_type', action='store', type=str, required=True, dest='int_type')

arg_parser.add_argument('--int_val', action='store', type=int, required=True, dest='int_val')

arg_parser.add_argument('--list_duble_type', action='store', type=str, required=True, dest='list_duble_type')

arg_parser.add_argument('--list_duble_val', action='store', type=str, required=True, dest='list_duble_val')

arg_parser.add_argument('--list_int_type', action='store', type=str, required=True, dest='list_int_type')

arg_parser.add_argument('--list_int_val', action='store', type=str, required=True, dest='list_int_val')

arg_parser.add_argument('--list_str_type', action='store', type=str, required=True, dest='list_str_type')

arg_parser.add_argument('--list_str_val', action='store', type=str, required=True, dest='list_str_val')

arg_parser.add_argument('--string_type', action='store', type=str, required=True, dest='string_type')

arg_parser.add_argument('--string_val', action='store', type=str, required=True, dest='string_val')


args = arg_parser.parse_args()
print(args)

id = args.id

float_type = args.float_type.replace('"','')
float_val = args.float_val
int_type = args.int_type.replace('"','')
int_val = args.int_val
list_duble_type = args.list_duble_type.replace('"','')
list_duble_val = json.loads(args.list_duble_val)
list_int_type = args.list_int_type.replace('"','')
list_int_val = json.loads(args.list_int_val)
list_str_type = args.list_str_type.replace('"','')
list_str_val = json.loads(args.list_str_val)
string_type = args.string_type.replace('"','')
string_val = args.string_val.replace('"','')



def check_type(value, expected_types: str):
    return True


check_type(int_val,int_type)
check_type(float_val,float_type)
check_type(string_val,string_type)
check_type(list_int_val,list_int_type)
check_type(list_duble_val,list_duble_type)
check_type(list_str_val,list_str_type)

