#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    args = sys.argv[1:]
    number_args = len(args)

    if number_args == 0:
        print("0 arguments.")
    else:
        print(f"{number_args} argument{'s' if number_args > 1 else ''}:")
        for index in range(number_args):
            print(f"{index+1}: {args[index]}")
