import random
import sys


def Enumerate_k_mers(in_file:str):
    res = []
    with open(in_file, "r") as file:
        lines = file.readlines()
    symbols = lines[0].split()
    pos = int(lines[1])
    while len(res) != (len(symbols) ** pos):
        sam = random.sample((symbols * pos), pos)
        if sam not in res:
            res.append(sam)
    return sorted(res)


if __name__ == "__main__":
    [print("".join(i)) for i in Enumerate_k_mers(sys.argv[1])]

# Also used random. But for this task it will plenty