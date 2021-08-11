#!/usr/bin/python

import os
import sys
import time

def main():
    # set up globals
    
    #in_filepath = "data/file1.txt"
    # check for program name & input file 
    if len(sys.argv) != 2:
        print('Error: incorrect number of arguments')
        print()
        print('Usage: {} inputfile'.format(sys.argv[0]))
        print()
        sys.exit(1)
    else:
        #OK, we have the right #. Grab the input filename
        in_filepath = sys.argv[1]
    
    out_filepath = "data/outfile1.txt"
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
