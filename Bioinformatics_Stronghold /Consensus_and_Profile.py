import sys
from Bio import SeqIO


def consensus(in_file:str):
    main_dict = {"A":[], "C":[], "G":[], "T":[]}
    for sequince in SeqIO.parse(in_file, "fasta"):
        for i, nucl in enumerate(sequince.seq):
            if len(main_dict[nucl]) == i:
                for nucl_key in main_dict.keys():
                    main_dict[nucl_key].append(0)
                main_dict[nucl][i] += 1
            else:
                main_dict[nucl][i] += 1
    consensus_seq = ""
    for n1, n2, n3, n4 in zip(main_dict["A"], main_dict["C"], main_dict["G"], main_dict["T"]):
        if n1 >= n2 and n1 >= n3 and n1 >= n4:
            consensus_seq += "A"
        elif n2 >= n1 and n2 >= n3 and n2 >= n4:
            consensus_seq += "C"
        elif n3 >= n2 and n3 >= n1 and n3 >= n4:
            consensus_seq += "G"
        else:
            consensus_seq += "T"
    print(consensus_seq)
    [print(f"{cons_list}: {' '.join(map(str, main_dict[cons_list]))}") for cons_list in main_dict]


if __name__ == "__main__":
    consensus(sys.argv[1])
