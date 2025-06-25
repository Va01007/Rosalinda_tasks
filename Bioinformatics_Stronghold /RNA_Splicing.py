import sys
from Bio import SeqIO


def RNA_Splice(in_file:str, acid_dict:dict):
    seq_list = []
    for i in SeqIO.parse(in_file, "fasta"):
        seq_list.append(str(i.seq))
    main_seq = seq_list[0]
    for seqince in seq_list[1:]:
        main_seq = main_seq.replace(seqince, "")
    main_seq = main_seq.replace("T", "U")
    prot = ""
    for nucl in range(0, len(main_seq), 3):
        prot += acid_dict[main_seq[nucl: nucl+3]]
    return prot[:-1]


if __name__ == "__main__":
    Acids = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "UAU":"Y", "UAC":"Y", "UAA":"!", "UAG":"!", \
"UGU":"C", "UGC":"C", "UGA":"!", "UGG":"W", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", \
"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", \
"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", \
"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", \
"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    print(RNA_Splice(sys.argv[1], Acids))
