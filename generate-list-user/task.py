import numpy as np

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




n = param_size * 1024 // 8  # float64 = 8 bytes
print(n)
a = np.random.random(n)

a_list = a.tolist()

print(f"a size: {a.nbytes / (1024**2):.2f} MB")

file_a_list = open("/tmp/a_list_" + id + ".json", "w")
file_a_list.write(json.dumps(a_list))
file_a_list.close()
