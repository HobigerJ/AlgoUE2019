import argparse
import time

parser = argparse.ArgumentParser(description="This program gives back either the n-th number or a list of the fibonacci series")
parser.add_argument("-n", type = int, help = "Use -n if you want to see the n-th number of the fibonacci series")
parser.add_argument("-all", type = int, help = "Use -all if you want to see a list of all fibonacci numbers up to the specified number")
args = parser.parse_args()

user_input_n = args.n
user_input_all = args.all


# rekursive Funktion: funktioniert!
def fib_rec(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


if args.all:
    F = [1]
    for i in range(2, user_input_all + 1):
        F.append(fib_rec(i))
    print(F)
else:
    print(fib_rec(user_input_n))
