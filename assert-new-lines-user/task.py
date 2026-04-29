
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--new_lines', action='store', type=str, required=True, dest='new_lines')


args = arg_parser.parse_args()
print(args)

id = args.id

new_lines = json.loads(args.new_lines)



assert new_lines == ['a_processed', 'b_processed', 'c_processed', 'd_processed', 'e_processed', 'f_processed', 'g_processed', 'h_processed', 'i_processed', 'j_processed', 'k_processed', 'l_processed', 'm_processed', 'n_processed', 'o_processed', 'p_processed', 'r_processed']

