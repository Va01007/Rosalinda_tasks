import sys
from Bio import SeqIO


def locate(in_file:str, Dictionar:dict):
    res = []
    for sequince in SeqIO.parse(in_file, "fasta"):
        for i, nucl in enumerate(sequince.seq):
            try:
                if f"{sequince.seq[i]}{sequince.seq[i+1]}" == f"{Dictionar[sequince.seq[i+3]]}{Dictionar[sequince.seq[i+2]]}":
                    res.append([i+1, 4])
                elif f"{sequince.seq[i]}{sequince.seq[i+1]}{sequince.seq[i+2]}" == f"{Dictionar[sequince.seq[i+5]]}{Dictionar[sequince.seq[i+4]]}{Dictionar[sequince.seq[i+3]]}":
                    res.append([i+1, 6])
                elif f"{sequince.seq[i]}{sequince.seq[i+1]}{sequince.seq[i+2]}{sequince.seq[i+3]}" == f"{Dictionar[sequince.seq[i+7]]}{Dictionar[sequince.seq[i+6]]}{Dictionar[sequince.seq[i+5]]}{Dictionar[sequince.seq[i+4]]}":
                    res.append([i+1, 8])
                elif f"{sequince.seq[i]}{sequince.seq[i+1]}{sequince.seq[i+2]}{sequince.seq[i+3]}{sequince.seq[i+4]}" == f"{Dictionar[sequince.seq[i+9]]}{Dictionar[sequince.seq[i+8]]}{Dictionar[sequince.seq[i+7]]}{Dictionar[sequince.seq[i+6]]}{Dictionar[sequince.seq[i+5]]}":
                    res.append([i+1, 10])
                elif f"{sequince.seq[i]}{sequince.seq[i+1]}{sequince.seq[i+2]}{sequince.seq[i+3]}{sequince.seq[i+4]}{sequince.seq[i+5]}" == f"{Dictionar[sequince.seq[i+11]]}{Dictionar[sequince.seq[i+10]]}{Dictionar[sequince.seq[i+9]]}{Dictionar[sequince.seq[i+8]]}{Dictionar[sequince.seq[i+7]]}{Dictionar[sequince.seq[i+6]]}":
                    res.append([i+1, 12])
            except:
                pass
    return res


if __name__ == "__main__":
    Nucl_dict = {"A":"T", "T":"A", "G":"C", "C":"G"}
    [print(f"{locations[0]} {locations[1]}") for locations in locate(sys.argv[1], Nucl_dict)]
