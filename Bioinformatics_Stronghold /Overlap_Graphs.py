import sys
from Bio import SeqIO


def Overlap(in_file:str):
    res = []
    for sequince in SeqIO.parse(in_file, "fasta"):
        for pair_seq in SeqIO.parse(in_file, "fasta"):
            if sequince.id == pair_seq.id:
                continue
            if sequince.seq[-3:] == pair_seq.seq[0:3]:
                res.append([sequince.id, pair_seq.id])
    return res


if __name__ == "__main__":
    [print(" ".join(match)) for match in Overlap(sys.argv[1])]
