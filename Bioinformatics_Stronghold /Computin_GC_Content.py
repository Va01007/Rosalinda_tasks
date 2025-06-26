import sys
from Bio import SeqIO


def GC_Computing(in_file:str):
    seq_dict = {}
    for i in SeqIO.parse(in_file, "fasta"):
        seq_dict[i.id] = str(i.seq)
    ID =  ""
    Content = 0
    for seq in seq_dict:
        GC = ((seq_dict[seq].count("G") + seq_dict[seq].count("C")) / len(seq_dict[seq])) * 100
        seq_dict[seq] = [GC]
        if Content < GC:
            ID = seq
            Content = GC
    return f"{ID}\n{Content}"

if __name__ == "__main__":
    print(GC_Computing(sys.argv[1]))
