"""Implement a program that accepts an integer via command line option -n and prints instructions to
STDOUT as follows:

Move disk from X to Y

Likewise, the tool should print the total number of disc move operations to STDERR upon
finishing the computation. Allow the user to obtain some information on your tool via a --help option.
The program should be named as

* $githubusername-TowersOfHanoi.$suffix -n [--help]

Once you are done with implementing the above tool you should measure the runtime within your shell. Ensure that
STDOUT is redirected to a file rather than displayed via the console (which would unnecessarily blow up runtime).
You might employ the concept of subshells to get this done.

Plot the runtime of your program (in seconds) vs size of the Hanoi puzzle and create a PDF graph.  """



import argparse

parser = argparse.ArgumentParser(description="This program gives back a manual on how to solve the problem of the hanoi towers with n disks")
parser.add_argument("-n", type = int, help = "Specify the number of disks with -n")
args = parser.parse_args()

user_input = args.n

counter = 0

def hanoi_towers(n, from_peg, to_peg):
    global counter

    if n == 1:
        print("Move disk from peg ", from_peg, "to peg ", to_peg)
        counter += 1

    elif n > 1:
        counter += 1

        unused_peg = 6 - from_peg - to_peg
        hanoi_towers(n-1, from_peg, unused_peg)
        print("Move disk from peg ", from_peg, "to peg ", to_peg)
        hanoi_towers(n-1, unused_peg, to_peg)


print(hanoi_towers(user_input, 1, 3), "\n", "count of operations: ", counter)
