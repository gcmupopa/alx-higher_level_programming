#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        intval = int(value)
        print("{:d}".format(intval))
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
