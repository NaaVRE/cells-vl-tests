import shutil
import os
from os import listdir
from os.path import isfile
from os.path import join

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id



conf_data_folder = conf_data_folder = os.path.join('/tmp', 'data')

L = ["a\n", "b\n", "c\n"]
file_path =  os.path.join(conf_data_folder,'hello.txt')
fp = open(file_path, 'w')
fp.writelines(L)
fp.close()

onlyfiles = [f for f in listdir(conf_data_folder) if isfile(join(conf_data_folder, f))]

print(onlyfiles)
naa_vre_user_data = '/home/jovyan/Cloud Storage/naa-vre-user-data/hello.txt'
shutil.copyfile(file_path, naa_vre_user_data)

file_file_path = open("/tmp/file_path_" + id + ".json", "w")
file_file_path.write(json.dumps(file_path))
file_file_path.close()
file_naa_vre_user_data = open("/tmp/naa_vre_user_data_" + id + ".json", "w")
file_naa_vre_user_data.write(json.dumps(naa_vre_user_data))
file_naa_vre_user_data.close()
