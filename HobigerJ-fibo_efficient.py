""" The task is to compute the the first n Fibonacci numbers. Implement an ineffieient as well as an efficient
version as two standalone programs that should accept an integer via command line option -n and print the
nth Fibonaci number to STDOUT. Implement an optional command line switch --all that prints all Fibonacci
numbers up to n as a comma-separated list to STDOUT. Document your tools accordinglt, i.e. provide at
least a --help switch that prints simple usage instructions to STDOUT. The file must be named according
to the following schema:

    $githubusername-fibo_inefficient.$suffix -n [--all] [--help]
    $githubusername-fibo_efficient.$suffix -n [--all] [--help]

Measure the runtime of both tools for different parameters of n, e.g. via the time command. Plot the
runtime of both approaches as a function of n in a single PDF graph. The filename should be
$githubusername-fibo_runtime.pdf. """


import argparse
import time

parser = argparse.ArgumentParser(description="This program gives back either the n-th number or a list of the fibonacci series")
parser.add_argument("-n", type = int, help = "Use -n if you want to see the n-th number of the fibonacci series")
parser.add_argument("-all", type = int, help = "Use -all if you want to see a list of all fibonacci numbers up to the specified number")
args = parser.parse_args()

user_input_n = args.n
user_input_all = args.all


def fib(n):
    F = [1,1]
    for i in range(2, n+1):
        x = F[i-1] + F[i-2]
        F.append(x)
    return F[n-1]


if args.all:
    F = [1,1]
    for i in range(2, user_input_all + 1):
        x = F[i-1] + F[i-2]
        F.append(x)
    print(F[0 : len(F)-1])
else:
    print(fib(user_input_n))
