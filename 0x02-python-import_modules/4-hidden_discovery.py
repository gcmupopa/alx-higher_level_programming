#!/usr/bin/python3

import sys
import hidden_4

if __name__ == '__main__':

    if sys.version_info[:2] != (3, 8):
        sys.exit()

    nam = dir(hidden_4)
    finam = [name for name in nam if not name.startswith("__")]
    sotname = sorted(finam)

    for name in sotname:
        print(name)
