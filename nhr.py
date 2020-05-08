#! /usr/bin/python2
import sys
import math

def nhr_eng(num):
    length = len(num)
    value = int(num)
    fmt = "{:>" + str(length - 1) + "d}"

    if value < pow(10, 3):
         return num;
    elif value < pow(10, 6):
        return fmt.format(value/ pow(10, 3)) + "K"
    elif value < pow(10, 9):
        return fmt.format(value/ pow(10, 6)) + "M"
    else:
        return fmt.format(value/ pow(10, 9)) + "G"



def nhr(line):
#    print line
    output = line
    start = 0
    while start < len(line):
        if line[start].isspace():
            start = start + 1
        else:
            for end in range(start+1, len(line)):
                if line[end].isspace():
                    if line[start:end].isdigit():
                        output = output[:start] + nhr_eng(line[start:end]) + output[end:]
                    start = end + 1
                    break                     
                else:
                    continue
    print output,

input = sys.stdin.readlines()
for line in input:
   nhr(line)
