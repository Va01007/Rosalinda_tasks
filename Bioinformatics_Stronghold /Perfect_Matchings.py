import sys
from Bio import SeqIO
import math


def perf_match(in_file:str):
    for i in SeqIO.parse(in_file, "fasta"):
        RNA = str(i.seq)
    arg1 = math.factorial(RNA.count("A")) // math.factorial(RNA.count("A") - RNA.count("U"))
    arg2 = math.factorial(RNA.count("G")) // math.factorial(RNA.count("G") - RNA.count("C"))
    perfect_match = arg1 * arg2
    return perfect_match


if __name__ == "__main__":
    print(perf_match(sys.argv[1]))
