import sys


def count_point_mutations(in_file:str, acid_dict:dict):
    with open(in_file, "r") as data:
        line = data.readlines()[0].rstrip("\n")
        prot = ""
        for nucl in range(len(line)):
            if nucl % 3 == 0:
                prot += acid_dict[line[nucl:(nucl + 3)]]
    return prot[:-1]


if __name__ == "__main__":
    Acids = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "UAU":"Y", "UAC":"Y", "UAA":"!", "UAG":"!", \
"UGU":"C", "UGC":"C", "UGA":"!", "UGG":"W", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", \
"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", \
"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", \
"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", \
"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    print(count_point_mutations(sys.argv[1], Acids))
