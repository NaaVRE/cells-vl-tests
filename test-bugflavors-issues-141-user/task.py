from dtAcolite import dtAcolite
import acolite as ac

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




ac.acolite.acolite_run(settings='')
inputfilenames = dtAcolite.create_acolite_input(app_configuration = '')

var = ''

file_var = open("/tmp/var_" + id + ".json", "w")
file_var.write(json.dumps(var))
file_var.close()
