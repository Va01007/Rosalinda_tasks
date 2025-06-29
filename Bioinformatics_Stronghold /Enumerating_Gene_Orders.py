import sys
import random 
from math import factorial


def EnumerateG(in_file:str):
    with open(in_file, "r") as data:
        n = int(data.readlines()[0])
    factN = factorial(n)
    value_list = []
    exit_list = []
    for i in range(n):
        value_list.append(i + 1)
    while len(exit_list) != factN:
        new_combine = random.sample(value_list, len(value_list))
        if new_combine in exit_list:
            continue
        else:
            exit_list.append(new_combine)
    print(factN)
    [print(" ".join(map(str, k))) for k in exit_list]


if __name__ == "__main__":
    EnumerateG(sys.argv[1])
