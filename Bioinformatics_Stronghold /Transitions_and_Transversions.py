import sys
from Bio import SeqIO


def Count_analisis(in_file:str):
    seq_list = []
    for i in SeqIO.parse(in_file, "fasta"):
        seq_list.append(str(i.seq))
        count_transitions = 0
        count_transversions = 0
    for nucl1, nucl2 in zip(seq_list[0], seq_list[1]):
        if nucl1 == nucl2:
            pass
        elif (nucl1 == "A" and nucl2 == "G") or (nucl1 == "G" and nucl2 == "A"):
            count_transitions += 1
        elif (nucl1 == "C" and nucl2 == "T") or (nucl1 == "T" and nucl2 == "C"):
            count_transitions += 1
        else:
            count_transversions += 1
    return ((count_transitions)/(count_transversions))


if __name__ == "__main__":
    print(Count_analisis(sys.argv[1]))
