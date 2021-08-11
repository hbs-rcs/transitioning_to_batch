#!/usr/bin/python

import os
import sys
import time
import argparse


def main():
    # set up globals
    
    #in_filepath = "data/file1.txt"
    import argparse
    # get inputs: either file name or data from STDIN
    parser = argparse.ArgumentParser(description='Process and sum values in input text files.')
    parser.add_argument('--input', '-i', required=True,
                        help='Filename of data to parse.')
    parser.add_argument('--output', '-o', required=True,
                        help='Filename of output for summed data.')
    
    args = parser.parse_args()
    
    if not(args.input):
        parser.error("Error: An input filename must be provided.")
    else:
        in_filepath = args.input
    if not(args.output):
        parser.error("Error: An output filename must be provided.")
    else:
        out_filepath = args.output
    #out_filepath = "data/outfile1.txt"
    
    status_count = 1000                 # when to give us status updates
    write_count = 10                    # when to write out running sum
    running_sum = 0

    # open our output file for continual updates, no buffering
    with open(out_filepath, mode='w') as out_fh:

        # open input datafile
        with open(in_filepath) as in_fh:

            for index, line in enumerate(in_fh):

                # sum, output, and give status when appropriate
                running_sum += int(line)

                # if at X line count, write out running sum (flush cache)
                if (index + 1) % write_count == 0:
                    out_fh.write(str(running_sum) + '\n')
                    out_fh.flush()

                # if at X line count, give us the status, and pause
                if (index + 1) % status_count == 0:
                    print("Line {}: {}".format(index + 1, running_sum))
                    time.sleep(0.25)



if __name__ == '__main__':
    main()
