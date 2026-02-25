import os

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_password = os.getenv('secret_password')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--file_path', action='store', type=str, required=True, dest='file_path')

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

arg_parser.add_argument('--new_lines', action='store', type=str, required=True, dest='new_lines')

arg_parser.add_argument('--new_list_duble_val', action='store', type=str, required=True, dest='new_list_duble_val')

arg_parser.add_argument('--new_list_int_val', action='store', type=str, required=True, dest='new_list_int_val')

arg_parser.add_argument('--string_type', action='store', type=str, required=True, dest='string_type')

arg_parser.add_argument('--string_val', action='store', type=str, required=True, dest='string_val')

arg_parser.add_argument('--param_with_dash', action='store', type=str, required=True, dest='param_with_dash')

args = arg_parser.parse_args()
print(args)

id = args.id

file_path = args.file_path.replace('"','')
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
new_lines = json.loads(args.new_lines)
new_list_duble_val = json.loads(args.new_list_duble_val)
new_list_int_val = json.loads(args.new_list_int_val)
string_type = args.string_type.replace('"','')
string_val = args.string_val.replace('"','')

param_with_dash = args.param_with_dash.replace('"','')

conf_data_folder = conf_data_folder = os.path.join('/tmp', 'data')
conf_user_folder = conf_user_folder = '/home/jovyan/Cloud Storage/naa-vre-user-data/'

assert ['Created using write mode._processed', 'Second line._processed', 'Third line._processed'] == new_lines


if not secret_password:
    raise ValueError('secret_password is empty.') 
if not conf_data_folder:
    raise ValueError('conf_data_folder is empty.') 
if not conf_user_folder:
    raise ValueError('conf_user_folder is empty.') 
if not param_with_dash:
    raise ValueError('param_with_dash is empty.')

assert secret_password == 'secret'
assert conf_data_folder == os.path.join('/tmp', 'data')
assert param_with_dash == '-param'


def check_type(value, expected_types: str):
    type_map = {
        "int": int,
        "float": float,
        "str": str,
        "bool": bool,
        "list": list,
        "tuple": tuple,
        "dict": dict,
        "set": set,
    }

    expected_type_names = [t.strip() for t in expected_types.split(",")]

    try:
        expected_type_objects = tuple(type_map[name] for name in expected_type_names)
    except KeyError as e:
        raise ValueError(f"Unsupported type name: {e.args[0]}")

    if not isinstance(value, expected_type_objects):
        raise TypeError(
            f"Expected type(s) {expected_types}, "
            f"but got {type(value).__name__}"
        )

    return True


check_type(int_val,int_type)
check_type(float_val,float_type)
check_type(string_val,string_type)
check_type(list_int_val,list_int_type)
check_type(list_duble_val,list_duble_type)
check_type(list_str_val,list_str_type)


assert os.path.exists(file_path)

content = ''
with open(file_path, "r") as file:
    content += file.read()

assert content == 'Created using write mode.\nSecond line.\nThird line.\n'
assert new_list_int_val == [2, 3, 4]
assert new_list_duble_val == [2.1, 3.1, 4.1]

