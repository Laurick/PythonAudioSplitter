# Audio splitter and merger for Python

## Description
Script for manage audio files in chunks using pydub library. Can take multiple params like:

-i for input(s) file(s)
-o for output path (will create the file)
-t for specify the maximun time of each split in milliseconds ( default 30 minutes )
-v for verbose output
-h for help


## Usage

### Spliter

The script can be launched easly with

`python3 spliter.py -i=./testFile.mp3`

That will create some files named "testFileX.mp3" at the same directory with the name "testFileX" ( where x is number of the chunk ) with splited audio of 30 minutes

`python3 spliter.py -i=./testFile.mp3 -o=~/Music/testFileSplitted -t=600000`

That will create some files named "testFileX.mp3" at the specified directory with the name "testFileSplittedX" ( where x is number of the chunk ) with splited audio of 10 minutes

### Merger

The script can be launched easly with

`python3 merger.py -i=./testFile1.mp3 ./testFile2.mp3 ./testFile3.mp3 -o ./testFileMerger.mp3`

That will create a file named "testFileMerger.mp3" at the same directory with the content of ./testFile1.mp3 ./testFile2.mp3 and ./testFile3.mp3 merged


## Requirements

- pydub

You can easy install the requirements using the requirements text file:

`pip install -r requirements.txt`

## Licence
CC0 1.0 Universal

## Version
1.1.0