#!/bin/bash

# Gets the directory for this script
# https://stackoverflow.com/questions/59895/how-to-get-the-source-directory-of-a-bash-script-from-within-the-script-itself
DIR=`dirname $0

for filename in "$DIR"/*.py; do
    filename="${filename##*/}" # removes proceeding directories from name
    filename="${filename%.*}" # removes extension from name

    cmd="python $DIR/$filename.py"
    alias $filename=$cmd # Creates an alias for the script being called
done