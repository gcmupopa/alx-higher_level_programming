import sys
from decimal import Decimal

args = sys.argv[1:]
number_args = len(args)
summ = Decimal(0)

for index in range(number_args):
    summ += Decimal(args[index])

print("summ")
