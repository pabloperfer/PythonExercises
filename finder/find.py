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

#I use os.walk for symbolic links as i need to exclude some special file systems like sys to not get a system error because too many levels of symlinks
def walk_error_handler(exception_instance):
    raise Exception('Exception')

def walk_sym(path):
    exclude=["proc","dev","sys"]
    for dirName, subdirList, fileList in os.walk(path,followlinks=True,topdown=True,onerror=walk_error_handler):
        for fname in fileList:
            subdirList[:] = [d for d in subdirList if d not in exclude]
            if fname == args.name:
                print (os.path.join(dirName,fname))


if args.type == ("-"):
    for i in walking_dir_tree_files(path):
        print(i)

elif args.type == ("d"):
    for i in walking_dir_tree_dirs(path):
        print(i)

elif args.type == ("l"):
    walk_sym(path)


