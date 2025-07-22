import sys
from Bio import SeqIO
import math


def max_match(in_file:str):
    for i in SeqIO.parse(in_file, "fasta"):
        RNA = str(i.seq)
    a = RNA.count("A")
    u = RNA.count("U")
    c = RNA.count("C")
    g = RNA.count("G")
    if a > u:
        arg1 = math.factorial(a) // math.factorial(a-u)
    else:
        arg1 = math.factorial(u) // math.factorial(u-a)
    if c > g:
        arg2 = math.factorial(c) // math.factorial(c-g)
    else:
        arg2 = math.factorial(g) // math.factorial(g-c)
    return int(arg1 * arg2)


if __name__ == "__main__":
    print(max_match(sys.argv[1]))

