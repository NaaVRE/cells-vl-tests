from obspy import UTCDateTime

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_channel', action='store', type=str, required=True, dest='param_channel')
arg_parser.add_argument('--param_duration_minutes', action='store', type=int, required=True, dest='param_duration_minutes')
arg_parser.add_argument('--param_location', action='store', type=str, required=True, dest='param_location')
arg_parser.add_argument('--param_networks', action='store', type=str, required=True, dest='param_networks')
arg_parser.add_argument('--param_provider', action='store', type=str, required=True, dest='param_provider')
arg_parser.add_argument('--param_stations', action='store', type=str, required=True, dest='param_stations')

args = arg_parser.parse_args()
print(args)

id = args.id


param_channel = args.param_channel.replace('"','')
param_duration_minutes = args.param_duration_minutes
param_location = args.param_location.replace('"','')
param_networks = args.param_networks.replace('"','')
param_provider = args.param_provider.replace('"','')
param_stations = args.param_stations.replace('"','')


        
      

def get_stream_and_inv(
        networks=param_networks,
        stations=param_stations,
        location=param_location,
        channel=param_channel,
        t0=UTCDateTime("2024-03-04 00:00:00"),
        duration_minutes=param_duration_minutes,
        fdsn_provider=param_provider,
        path_storage="/tmp/data"
    ):
    '''
        Returns the paths of converted stream and inventory files for containerisation.

        Parameters (edit me):
    '''
    




    
    path_stream = f"{path_storage}/stream.mseed"
    print(f"Successfully transported stream to {path_stream}")

    path_inv = f"{path_storage}/inv.xml"
    print(f"Successfully transported inventory to {path_inv}")
    
    return path_stream, path_inv

dir_stream, dir_inv = get_stream_and_inv()

file_dir_stream = open("/tmp/dir_stream_" + id + ".json", "w")
file_dir_stream.write(json.dumps(dir_stream))
file_dir_stream.close()
