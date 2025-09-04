import sys
from Bio import SeqIO


def Complementing(in_file:str):
    counter = 0
    for i in SeqIO.parse(in_file, "fasta"):
        rev_comp = i.reverse_complement()
        if i.seq == rev_comp.seq:
            counter += 1
    return counter


if __name__ == "__main__":
    print(Complementing(sys.argv[1]))
