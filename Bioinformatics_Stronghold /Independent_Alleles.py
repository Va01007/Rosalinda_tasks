import math
import sys


def Alleles(in_file:str):
    with open(in_file, "r") as file:
        line = file.readline()
        k = int(line.split()[0])
        N = int(line.split()[1])
    count_creature = 2 ** k
    res = {i: (0.75 ** (count_creature - i)) * (0.25 ** i) for i in range(N)}
    end = 0
    for item in res.keys():
        end += res[item] * math.comb(count_creature, item)
    anti = round(end, 3)
    return (1 - end)


if __name__ == "__main__":
    print(Alleles(sys.argv[1]))
