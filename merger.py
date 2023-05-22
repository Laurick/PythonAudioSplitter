import pydub
import numpy as np
import argparse
import pathlib
import os

DEFAULT_SPLIT_TIME = 30*60*1000 # 30 minutes

parser = argparse.ArgumentParser(description='audio merge, merge audio filed in one')
parser.add_argument('-i', '--inputs', nargs='+', type=pathlib.Path, help='inputs file for merge', required=True)
parser.add_argument('-o', '--output', type=pathlib.Path, help='output for merged file', required=False)
parser.add_argument('-v', '--verbose', help='print info about the state', type=bool, default=False, required=False)

args = parser.parse_args()
variables = vars(args)

input_files_names = variables['inputs']
verbose_output = variables['verbose']

output_file_name = variables['inputs']
if variables['output'] is not None:
    output_file_name = variables['output']
else:
    output_file_name = os.path.splitext(input_files_names[0])[0]

if verbose_output: 
    print("Merging"+str(input_files_names))

combinedAudios = pydub.AudioSegment.from_file(input_files_names[0])

max_audios = len(input_files_names)
for index in range(1,max_audios):
    nextAudio = pydub.AudioSegment.from_file(input_files_names[index])
    combinedAudios += nextAudio

# simple export
file_handle = combinedAudios.export(output_file_name, format="mp3")