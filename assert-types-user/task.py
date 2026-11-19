
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
expected_arg_names.add('float_type')
expected_arg_names.add('float_val')
expected_arg_names.add('int_type')
expected_arg_names.add('int_val')
expected_arg_names.add('list_double_element_type')
expected_arg_names.add('list_double_type')
expected_arg_names.add('list_double_val')
expected_arg_names.add('list_int_element_type')
expected_arg_names.add('list_int_type')
expected_arg_names.add('list_int_val')
expected_arg_names.add('list_str_element_type')
expected_arg_names.add('list_str_type')
expected_arg_names.add('list_str_val')
expected_arg_names.add('string_type')
expected_arg_names.add('string_val')
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

arg_name = 'float_type'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
float_type = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'float_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = float
float_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'int_type'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
int_type = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'int_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = int
int_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'list_double_element_type'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
list_double_element_type = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'list_double_type'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
list_double_type = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'list_double_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = list
list_double_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'list_int_element_type'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
list_int_element_type = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'list_int_type'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
list_int_type = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'list_int_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = list
list_int_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'list_str_element_type'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
list_str_element_type = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'list_str_type'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
list_str_type = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'list_str_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = list
list_str_val = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'string_type'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
string_type = _parse_value(arg_value, arg_name, arg_type)
arg_name = 'string_val'
arg_value = get_arg_value(arg_name,args,raw_args)
arg_type = str
string_val = _parse_value(arg_value, arg_name, arg_type)



arg_value = get_arg_value('id',args,raw_args)
id = _parse_value(arg_value, 'id', str)

def check_type(value, expected_type: str, element_type: str = None):
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

    if expected_type not in type_map:
        raise ValueError(f"Unsupported type name: {expected_type}")

    if not isinstance(value, type_map[expected_type]):
        raise TypeError(
            f"Expected type {expected_type}, "
            f"but got {type(value).__name__}"
        )

    if element_type is not None:
        if expected_type not in {"list", "tuple", "set"}:
            raise TypeError(
                f"Element type checking is only supported for list, tuple, and set"
            )

        if element_type not in type_map:
            raise ValueError(f"Unsupported element type name: {element_type}")

        element_python_type = type_map[element_type]

        if not all(isinstance(item, element_python_type) for item in value):
            raise TypeError(
                f"All elements must be of type {element_type}"
            )

    return True

check_type(int_val, int_type)  # True
check_type(float_val, float_type)
check_type(string_val, string_type)  
check_type(list_int_val, list_int_type, list_int_element_type)
check_type(list_double_val, list_double_type, list_double_element_type)
check_type(list_str_val, list_str_type, list_str_element_type)

