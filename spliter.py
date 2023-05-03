import pydub
import argparse
import pathlib
import os

DEFAULT_SPLIT_TIME = 30*60*1000 # 30 minutes

parser = argparse.ArgumentParser(description='audio spliter, split audio file in chunks')
parser.add_argument('-i', '--input', type=pathlib.Path, help='input file for split', required=True)
parser.add_argument('-o', '--output', type=pathlib.Path, help='output for splitted files', required=False)
parser.add_argument('-t', '--time', type=int, help='max time of each split in MILLISECONDS', default=DEFAULT_SPLIT_TIME, required=False)
parser.add_argument('-v', '--verbose', help='print info about the state', type=bool, default=False, required=False)

args = parser.parse_args()
variables = vars(args)

input_file_name = variables['input']
verbose_output = variables['verbose']

output_file_name = variables['input']
if variables['output'] is not None:
    output_file_name = variables['output']
else:
    output_file_name = os.path.splitext(variables['input'])[0]

time_of_each_split = variables['time']

if verbose_output: 
    print("Reading file: "+str(input_file_name))
sound_file = pydub.AudioSegment.from_mp3(input_file_name)
ranges = []
last_time_checkpoint = 0
duration_in_millis = len(sound_file)
for time_checkpoint in range(time_of_each_split, duration_in_millis, time_of_each_split):
    ranges.append((last_time_checkpoint,time_checkpoint))
    last_time_checkpoint = time_checkpoint

ranges.append((last_time_checkpoint,duration_in_millis))

if verbose_output: 
    print("Slices: "+str(len(ranges)))
    print("Times: "+str(ranges))

index = 0
# milliseconds in the sound track
for start, end in ranges:
    if verbose_output: 
        print("Slicing chunk "+ str(index))
    chunk=sound_file[start : end]
    chunk.export(str(output_file_name) + str(index) +".mp3", format="mp3")
    index+=1