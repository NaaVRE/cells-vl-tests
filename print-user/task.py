
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




int_val = 1
int_type = 'int'

float_val = 1.0
float_type = 'float'

string_val ='1'
string_type = 'str'

list_int_val = [1,2,3]
list_int_type = 'list'

list_duble_val = [1.0,2.0,3.0]
list_duble_type = 'list'

list_str_val = ["1","2","3"]
list_str_type = 'list'

file_float_type = open("/tmp/float_type_" + id + ".json", "w")
file_float_type.write(json.dumps(float_type))
file_float_type.close()
file_float_val = open("/tmp/float_val_" + id + ".json", "w")
file_float_val.write(json.dumps(float_val))
file_float_val.close()
file_int_type = open("/tmp/int_type_" + id + ".json", "w")
file_int_type.write(json.dumps(int_type))
file_int_type.close()
file_int_val = open("/tmp/int_val_" + id + ".json", "w")
file_int_val.write(json.dumps(int_val))
file_int_val.close()
file_list_duble_type = open("/tmp/list_duble_type_" + id + ".json", "w")
file_list_duble_type.write(json.dumps(list_duble_type))
file_list_duble_type.close()
file_list_duble_val = open("/tmp/list_duble_val_" + id + ".json", "w")
file_list_duble_val.write(json.dumps(list_duble_val))
file_list_duble_val.close()
file_list_int_type = open("/tmp/list_int_type_" + id + ".json", "w")
file_list_int_type.write(json.dumps(list_int_type))
file_list_int_type.close()
file_list_int_val = open("/tmp/list_int_val_" + id + ".json", "w")
file_list_int_val.write(json.dumps(list_int_val))
file_list_int_val.close()
file_list_str_type = open("/tmp/list_str_type_" + id + ".json", "w")
file_list_str_type.write(json.dumps(list_str_type))
file_list_str_type.close()
file_list_str_val = open("/tmp/list_str_val_" + id + ".json", "w")
file_list_str_val.write(json.dumps(list_str_val))
file_list_str_val.close()
file_string_type = open("/tmp/string_type_" + id + ".json", "w")
file_string_type.write(json.dumps(string_type))
file_string_type.close()
file_string_val = open("/tmp/string_val_" + id + ".json", "w")
file_string_val.write(json.dumps(string_val))
file_string_val.close()
