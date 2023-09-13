#!/usr/bin/python3
import sys

"""
This module defines a script that reads stdin line by line and computes metrics

"""

def comp_metric():
    """
    reads stdin line by line and computes metrics

    """        
    tots_filesize = 0
    stat_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    linecount = 0

    try:
        for line in sys.stdin:
            linecount += 1

            part = line.split()
            filesize = int(part[-1])
            statcode = int(part[-2])

            tots_filesize += filesize

            if statcode in stat_count:
                stat_count[statcode] += 1

            if linecount % 10 == 0:
                print("Total file size:", tots_filesize)
                for code in sorted(stat_count):
                    counter = stat_count[code]
                    if counter > 0:
                        print(f"{code}: {counter}")

    except KeyboardInterrupt:
        print("Total file size", tots_filesize)
        for code in sorted(stat_count):
            counter = stat_count[code]
            if counter > 0:
                print(f"{code}: {counter}")

comp_metric()
    
