import sys


def Infer_mRNA(in_file:str):
    with open(in_file, "r") as file:
        protline = file.readlines()[0][:-1] + "!"
    fin = 1
    for i in protline:
        fin = fin * prot_dict[i]
    return fin % 1000000


if __name__ == "__main__":
    prot_dict = {"F":2, "L":6, "S":6, "Y":2, "!":3, "W":1, "P":4, "H":2, "Q":2, "R":6, "I":3, "M":1, "V":4, "A":4, "D":2, "E":2, "G":4, "K":2, "T":4, "N":2, "C":2}
    print(Infer_mRNA(sys.argv[1]))

#yeah, it was without modular arithmetic. But if i can do this how will stop me?