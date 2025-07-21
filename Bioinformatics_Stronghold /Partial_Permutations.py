import sys
import math


def partial_perm(in_file:str):
    with open(in_file, "r") as file:
        breaks = (file.readlines()[0]).split()
        res = math.factorial(int(breaks[0])) / (math.factorial(int(breaks[0]) - int(breaks[1])))
    return int(math.fmod(res, 1000000))


if __name__ == "__main__":
    print(partial_perm(sys.argv[1]))
