import sys, subprocess, os
from Bio import SeqIO


def Local_aligment(in_file:str):
    Base_path = os.path.dirname(os.path.realpath(__file__))
    counter = 0
    seq_list = []
    for i in SeqIO.parse(in_file, "fasta"):
        seq_list.append(str(i.seq))
    share_list = []
    for num, symb in enumerate(seq_list[0]):
        if symb in seq_list[1]:
            temp_str = f"{symb}"
            for add_symb in seq_list[0][(num+1):]:
                temp_str += add_symb
                if temp_str in seq_list[1]:
                    pass
                else:
                    share_list.append(temp_str[:-1])
                    break
    with open(f"{Base_path}/temp_seq.fasta", "w") as OUT:
        OUT.write(f">TestSEQ\n")
        OUT.write(f"{max(share_list, key =len)}")
    result = subprocess.run([f"lalign36 {Base_path}/temp_seq.fasta {in_file}"], 
                                      capture_output=True, text=True, shell=True)
    os.remove(f"{Base_path}/temp_seq.fasta")
    return result.stdout


if __name__ == "__main__":
    print(Local_aligment(sys.argv[1]))
