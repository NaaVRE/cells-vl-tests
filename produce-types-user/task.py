
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




arg_value = get_arg_value('id',args,raw_args)
id = _parse_value(arg_value, 'id', str)

int_val = 1
int_type = 'int'

float_val = 1.0
float_type = 'float'

string_val ='hello.txt'
string_type = 'str'

list_int_val = [1,2,3]
list_int_type = 'list'
list_int_element_type = int_type

list_double_val = [1.0,2.0,3.0]
list_double_type = 'list'
list_double_element_type = float_type

list_str_val = ["1","2","3"]
list_str_type = 'list'
list_str_element_type = string_type

file_int_val = open("/tmp/int_val_" + id + ".json", "w")
file_int_val.write(json.dumps(int_val))
file_int_val.close()
file_int_type = open("/tmp/int_type_" + id + ".json", "w")
file_int_type.write(json.dumps(int_type))
file_int_type.close()
file_float_val = open("/tmp/float_val_" + id + ".json", "w")
file_float_val.write(json.dumps(float_val))
file_float_val.close()
file_float_type = open("/tmp/float_type_" + id + ".json", "w")
file_float_type.write(json.dumps(float_type))
file_float_type.close()
file_string_val = open("/tmp/string_val_" + id + ".json", "w")
file_string_val.write(json.dumps(string_val))
file_string_val.close()
file_string_type = open("/tmp/string_type_" + id + ".json", "w")
file_string_type.write(json.dumps(string_type))
file_string_type.close()
file_list_int_val = open("/tmp/list_int_val_" + id + ".json", "w")
file_list_int_val.write(json.dumps(list_int_val))
file_list_int_val.close()
file_list_int_type = open("/tmp/list_int_type_" + id + ".json", "w")
file_list_int_type.write(json.dumps(list_int_type))
file_list_int_type.close()
file_list_int_element_type = open("/tmp/list_int_element_type_" + id + ".json", "w")
file_list_int_element_type.write(json.dumps(list_int_element_type))
file_list_int_element_type.close()
file_list_double_val = open("/tmp/list_double_val_" + id + ".json", "w")
file_list_double_val.write(json.dumps(list_double_val))
file_list_double_val.close()
file_list_double_type = open("/tmp/list_double_type_" + id + ".json", "w")
file_list_double_type.write(json.dumps(list_double_type))
file_list_double_type.close()
file_list_double_element_type = open("/tmp/list_double_element_type_" + id + ".json", "w")
file_list_double_element_type.write(json.dumps(list_double_element_type))
file_list_double_element_type.close()
file_list_str_val = open("/tmp/list_str_val_" + id + ".json", "w")
file_list_str_val.write(json.dumps(list_str_val))
file_list_str_val.close()
file_list_str_type = open("/tmp/list_str_type_" + id + ".json", "w")
file_list_str_type.write(json.dumps(list_str_type))
file_list_str_type.close()
file_list_str_element_type = open("/tmp/list_str_element_type_" + id + ".json", "w")
file_list_str_element_type.write(json.dumps(list_str_element_type))
file_list_str_element_type.close()
