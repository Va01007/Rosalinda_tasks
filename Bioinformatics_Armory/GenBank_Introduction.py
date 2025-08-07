import sys
from Bio import Entrez


def req(in_file:str):
    with open(in_file, "r") as file:
        lines = file.readlines()
    handle = Entrez.esearch(db="nucleotide", term=f'"{lines[0]}"[Organism] AND "{lines[1]}":"{lines[2]}"[PDAT]', )
    record = Entrez.read(handle)
    return record['Count']


if __name__ == "__main__":
    print(req(sys.argv[1]))
