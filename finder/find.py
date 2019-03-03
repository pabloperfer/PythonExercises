import argparse
import os, sys
from os import scandir
import glob


#We create an ArgumentParser object that will hold all the info to parse the command line into Python data types.
parser = argparse.ArgumentParser()

parser.add_argument("path", help="Enter the path where you want to search the file")
parser.add_argument("name", help="Enter the name of the file you look for")
parser.add_argument('type',  help = "Enter the type of file you are looking for from the above choices", choices=['-', 'd', 'l'])


#ArgumentParser object by means of parse_args() method inspect the command line, convert each argument and invoke the appropriate action.

args = parser.parse_args()
path = args.path



#we raise an exception if the path provided is not an existing directory
if not os.path.isdir(path):
    raise Exception('the path should be a dir ')

# functions for each file type to get files in the path

def walking_dir_tree_files(path):
    for entry in scandir(path):  
        if entry.is_dir(follow_symlinks=False):
            yield from walking_dir_tree_files(entry.path) 
        elif (entry.is_file(follow_symlinks=False) and entry.name == args.name):
            yield os.path.join(path,entry.name)

def walking_dir_tree_dirs(path):
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False) and (entry.name == args.name):
            yield os.path.join(path,entry.name)
        if entry.is_dir(follow_symlinks=False):
            yield from walking_dir_tree_dirs(entry.path)

def walking_dir_tree_simb(path):
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from walking_dir_tree_files(entry.path)
        if entry.is_symlink() and entry.name == args.name:
            yield os.path.join(path,entry.name)

if args.type == ("-"):
    for i in walking_dir_tree_files(path):
        print(i)

elif args.type == ("d"):
    for i in walking_dir_tree_dirs(path):
        print(i)

elif args.type == ("l"):
    for i in walking_dir_tree_simb(path):
        print(i)



  
    
