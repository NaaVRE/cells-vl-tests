import json

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--dir_stream', action='store', type=str, required=True, dest='dir_stream')

arg_parser.add_argument('--param_batch_size', action='store', type=int, required=True, dest='param_batch_size')
arg_parser.add_argument('--param_p_thld', action='store', type=float, required=True, dest='param_p_thld')
arg_parser.add_argument('--param_s_thld', action='store', type=float, required=True, dest='param_s_thld')

args = arg_parser.parse_args()
print(args)

id = args.id

dir_stream = args.dir_stream.replace('"','')

param_batch_size = args.param_batch_size
param_p_thld = args.param_p_thld
param_s_thld = args.param_s_thld


    

    

def get_picks(path_stream, batch_size=param_batch_size, p_thld=param_p_thld, s_thld=param_s_thld):
    '''Picks phases (only if we have data).

    Args:
        path_stream: directory to the converted stream file.
    Parameters (edit me):
        BATCH_SIZE = 128
        P_THRESHOLD = 0.10
        S_THRESHOLD = 0.10

    Returns: JSON file of the picks
    '''

    

    
    list_picks = [{"a": "a"}]
    json_picks = json.dumps(list_picks)
    print("Picks process completed: Converted to JSON file.")
    return json_picks

dir_json_picks = get_picks(path_stream=dir_stream)

