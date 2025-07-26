import sys
import math
import random
from Bio import SeqIO


def Composition(in_file:str):
    limiter = 256 # the number of combinations of 4 symbols with the condition of possible repetitions of symbols, calculated separately and this value is constanta
    k_mer_list = []
    ### set list of possible k-mers
    while len(k_mer_list) != limiter:
        random_k_mer_list = random.choices(["A", "C", "T", "G"], k = 4)
        random_k_mer = "".join(random_k_mer_list)
        if (random_k_mer) in k_mer_list:
            continue
        else:
            k_mer_list.append(random_k_mer)
    ### order list
    main_list = sorted(k_mer_list)
    main_dict = {k_from_list:0 for k_from_list in main_list}
    ### finding all possible k-mers
    for i in SeqIO.parse(in_file, "fasta"):
        for nucl in range(len(i.seq)-3):
            if i.seq[nucl:nucl+4] in main_dict:
                main_dict[i.seq[nucl:nucl+4]] +=1
    
    result_list = [main_dict[x] for x in main_dict]
    return " ".join(map(str, result_list))


if __name__ == "__main__":
    print(Composition(sys.argv[1]))



