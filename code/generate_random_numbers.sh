#!/bin/bash
# Script generates 20,000 random numbers
# taken from https://blog.eduonix.com/shell-scripting/generating-random-numbers-in-linux-shell-scripting/
# Author: Eduonix
# Date: Oct 2015

limit=2000000

# if parameter is missing, barf Usage
if [ -z "$1" ];
then
    echo "Usage: $0 filename"
    exit 1
fi

# if file exists, barf with warning
if [ -e "$1" ]; 
then
    echo "Error: file $1 already exists"
    exit 1
fi

# OK, let's output our X random numbers
RANDOM=$$
for i in `seq $limit`
do
  echo $RANDOM >> "$1"
done
