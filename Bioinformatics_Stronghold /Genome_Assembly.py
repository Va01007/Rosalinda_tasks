import sys
from Bio import SeqIO


def As_superstring(in_file:str):
    seq_dict = {}
    for i in SeqIO.parse(in_file, "fasta"):
        seq_dict[str(i.seq)] = 0
    super_string = ""
    counter = 0
    while sum(seq_dict.values()) != len(seq_dict):
        for seq in seq_dict.keys():
            if seq_dict[seq] == 1:
                continue
            if super_string == "":
                super_string = seq
                seq_dict[seq] = 1
                counter = len(seq)
            elif seq in super_string:
                seq_dict[seq] = 1
            else:
                if seq[-counter:] == super_string[:counter]:
                    super_string = seq[:-counter] + super_string
                    counter = len(seq)
                    seq_dict[seq] = 1
                elif seq[:counter] == super_string[-counter:]:
                    super_string =  super_string + seq[counter:]
                    counter = len(seq)
                    seq_dict[seq] = 1
        counter -= 1
    return super_string


if __name__ == "__main__":
    print(As_superstring(sys.argv[1]))

#Genome Assembly as Shortest Superstring