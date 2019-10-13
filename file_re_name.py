import re 
import os 
from os import listdir
from os.path import isfile, join

# Sample dir /Users/hellspawn/Downloads/Anime/One Piece

# Valid regex for an anime file name
valid_regex = r'(\x5b([A-Za-z]*)\x5d)([0-9\x20A-Za-z]* )([\x20\x2d\x20])(\x20[0-9]*\x20)(\x5b([A-Za-z0-9]*)\x5d)(\x2e([A-Za-z0-9]*))'

# Fansub name [HorribleSubs]
fansub_name = r'(\x5b([A-Za-z]*)\x5d)'
# File name One Piece - 100
file_name = r'([0-9\x20A-Za-z]* )([\x20\x2d\x20])(\x20[0-9]*\x20)'
# File resolution [1080p]
file_res = r'(\x20\x5b([A-Za-z0-9]*)\x5d)'
# File extension .mkv
ext = r'(\x2e([A-Za-z0-9]*))'
# File extension helper $.
file_ext = r'(\x24\x2e)'

# Reads directory and only fetches files with valid regex 
def read_directory(directory):
    rex = re.compile(valid_regex)
    files = [f for f in listdir(directory) if isfile(join(directory, f)) and rex.search(f) is not None]
    return files 

# Returns the appropiate re named file name for a file 
def get_renamed_file_name(original_file_name):
    return re.sub(fansub_name, '', re.sub(file_ext, '.', re.sub(file_res, '$', original_file_name))).strip()

# Renames all valid files on directory
def rename_files(directory):
    files_to_rename = read_directory(directory)
    directory += '/'
    for f in files_to_rename: 
        os.rename(directory + f, directory + get_renamed_file_name(f))

rename_files('/Users/hellspawn/Downloads/Anime/One Piece')