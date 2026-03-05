from datetime import datetime

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




now = str(datetime.today())

file_now = open("/tmp/now_" + id + ".json", "w")
file_now.write(json.dumps(now))
file_now.close()
