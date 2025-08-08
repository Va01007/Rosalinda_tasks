import sys
from Bio import Entrez
from Bio import SeqIO


def data_format(in_file:str):
    with open(in_file, "r") as file:
        ids = [file.readlines()[0]]
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
    temp_min_length = ["id", 0]
    for i in SeqIO.parse(handle, "fasta"):
        if temp_min_length[1] == 0:
            temp_min_length = [i.id, len(i.seq)]
        elif temp_min_length[1] > len(i.seq):
            temp_min_length = [i.id, len(i.seq)]
    new_handle = Entrez.efetch(db="nucleotide", id=[temp_min_length[0]], rettype="fasta")
    return (new_handle.read())


if __name__ == "__main__":
    print(data_format(sys.argv[1]))
