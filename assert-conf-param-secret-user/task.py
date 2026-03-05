
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_string_val = os.getenv('secret_string_val')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_float_val', action='store', type=float, required=True, dest='param_float_val')
arg_parser.add_argument('--param_int_val', action='store', type=int, required=True, dest='param_int_val')
arg_parser.add_argument('--param_list_double_val', action='store', type=str, required=True, dest='param_list_double_val')
arg_parser.add_argument('--param_list_int_val', action='store', type=str, required=True, dest='param_list_int_val')
arg_parser.add_argument('--param_list_str_val', action='store', type=str, required=True, dest='param_list_str_val')
arg_parser.add_argument('--param_string_val', action='store', type=str, required=True, dest='param_string_val')

args = arg_parser.parse_args()
print(args)

id = args.id


param_float_val = args.param_float_val
param_int_val = args.param_int_val
print(args.param_list_double_val)
print(type(args.param_list_double_val))
try:
    param_list_double_val = json.loads(args.param_list_double_val)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
        param_list_double_val = ast.literal_eval(args.param_list_double_val.replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e
print(args.param_list_int_val)
print(type(args.param_list_int_val))
try:
    param_list_int_val = json.loads(args.param_list_int_val)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
        param_list_int_val = ast.literal_eval(args.param_list_int_val.replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e
print(args.param_list_str_val)
print(type(args.param_list_str_val))
try:
    param_list_str_val = json.loads(args.param_list_str_val)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
        param_list_str_val = ast.literal_eval(args.param_list_str_val.replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e
param_string_val = args.param_string_val.replace('"','')

conf_int_val = conf_int_val = 1
conf_float_val = conf_float_val = 1.0
conf_string_val = conf_string_val = '-param'
conf_list_int_val = conf_list_int_val = [1, 2, 3]
conf_list_double_val = conf_list_double_val = [1.0, 2.0, 3.0]
conf_list_str_val = conf_list_str_val = ['1', '2', '3']

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

