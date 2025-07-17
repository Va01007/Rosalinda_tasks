import sys
from Bio import SeqIO


def Splice_motif(in_file:str):
    res = []
    seq_list = []
    for i in SeqIO.parse(in_file, "fasta"):
        seq_list.append(str(i.seq))
    sample_seq = list(seq_list[1])
    counter = 0
    for target in sample_seq:
        for nucl in seq_list[0][counter:]:
            if target == nucl:
                res.append(counter+1)
                counter += 1
                break
            counter += 1
    return "\t".join(map(str, res))


if __name__ == "__main__":
    print(Splice_motif(sys.argv[1]))
