
import argparse
import json
import os

def _load_json_args(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def _parse_value(value, field_name, target_type, elem_type=None):
    if target_type is list:
        if isinstance(value, list):
            return value
        elif isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                # the value may be "['list_str', 'space in elem', '3']"
                if value.startswith('[') and value.endswith(']'):
                    value = value[1:-1].strip()  # remove the brackets and trim whitespace
                    if value:
                        return [elem.strip().strip("'").strip('"') for elem in value.split(',')]
                    else:
                        return []
                else:
                    arg_parser.error(field_name + " is not a valid list")

    if target_type is str:
        return value

    if target_type is int:
        return int(value)

    if target_type is float:
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            return float(value)
    arg_parser.error(field_name + " has unsupported target type")

def get_arg_value(name,args,raw_args):
    for arg in raw_args:
        if arg['name'] == name:
            return arg['value']
    arg_parser.error("Argument '" + name + "' not found in JSON args")

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--args_json', action='store', type=str, required=True, dest='args_json')

args = arg_parser.parse_args()

expected_arg_names = set()
expected_arg_names.add('param_float_val')
expected_arg_names.add('param_int_val')
expected_arg_names.add('param_list_double_val')
expected_arg_names.add('param_list_int_val')
expected_arg_names.add('param_list_str_val')
expected_arg_names.add('param_string_val')
expected_arg_names.add('conf_float_val')
expected_arg_names.add('conf_int_val')
expected_arg_names.add('conf_list_double_val')
expected_arg_names.add('conf_list_int_val')
expected_arg_names.add('conf_list_str_val')
expected_arg_names.add('conf_string_val')
expected_arg_names.add('id')

raw_args = _load_json_args(args.args_json)
for arg in raw_args:
    if 'name' not in arg:
        arg_parser.error("Argument with no name found in JSON args")
    if arg['name'] not in expected_arg_names:
        arg_parser.error("Unexpected argument '" + arg['name'] + "' found in JSON args")
    if not arg['name'].startswith('conf'):
            if 'value' not in arg or arg['value'] is None:
                arg_parser.error("Argument '" + arg['name'] + "' has no value in JSON args")
    if arg['name'].startswith('conf'):
            if 'assignation' not in arg or arg['assignation'] is None:
                arg_parser.error("Argument '" + arg['name'] + "' has no assignation in JSON args")

arg_name = 'param_float_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = float
param_float_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'param_int_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = int
param_int_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'param_list_double_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = list
param_list_double_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'param_list_int_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = list
param_list_int_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'param_list_str_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = list
param_list_str_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'param_string_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
param_string_val = _parse_value(arg_value, arg_name, arg_type)

conf_float_val = 1.0
conf_int_val = 1
conf_list_double_val = [1.0, 2.0, 3.0]
conf_list_int_val = [1, 2, 3]
conf_list_str_val = ['1', '2', '3']
conf_string_val = '-param'

secret_string_val = os.getenv('secret_string_val')

arg_value = get_arg_value('id',args,raw_args)
id = _parse_value(arg_value, 'id', str)

assert conf_int_val == 1
assert conf_float_val == 1.0
assert conf_string_val =='-param'
assert conf_list_int_val == [1,2,3]
assert conf_list_double_val == [1.0,2.0,3.0]
assert conf_list_str_val == ["1","2","3"]

assert param_int_val == 1
assert param_float_val == 1.0
assert param_string_val =='-param'
assert param_list_int_val == [1,2,3]
assert param_list_double_val == [1.0,2.0,3.0]
assert param_list_str_val == ["1","2","3"]

assert secret_string_val =='secret'

