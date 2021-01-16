import argparse, sys

parser = argparse.ArgumentParser(description='Sorts files in a directory into subfolders off their ext.')

parser.add_argument('dir', default='.',
    help="The directory to sort the files"
)
parser.add_argument('--destination', default='.',
    help='The directory underneath the sorted directory to store the sorted files'
)


args = parser.parse_args()

from os.path import join, exists, isdir, abspath, splitext, basename
from os import renames, listdir

from multiprocessing import Pool

dirname = args.dir

def sort_file(pathname):
    """Sorts the path if it is not a directory."""
    
    file = join(dirname, pathname)
    if isdir(file): return

    name, ext = splitext(pathname)

    new = join(dirname, args.destination, ext, pathname)
    try: renames(file, new)
    except Exception as e: print(str(e))

def main():
    
    # Check if isdir
    if not exists(dirname) or not isdir(dirname): 
        sys.exit("dir given is not a directory")
    
    # Exit if unsure
    response = input(f"Are you sure you want to sort the files in {abspath(dirname)}: ")
    if response.lower() not in ['yes', 'y']: sys.exit(0)

    files = list(listdir(dirname))
    with Pool(len(files)) as pool:
        pool.map(sort_file, files)

if __name__ == '__main__':
    main() # dirname