import sys, subprocess, os
from Bio import SeqIO


def find_orfs(in_file:str):
    Base_path = os.path.dirname(os.path.realpath(__file__))
    result = subprocess.run([f"getorf -sequence {in_file} -table 1 -find 1 -outseq {Base_path}/prot1.txt"], 
                                      capture_output=False, text=False, shell=True)
    prot_list = []
    for i1 in SeqIO.parse(f"{Base_path}/prot1.txt", "fasta"):
        prot_list.append(str(i1.seq))
    os.remove(f"{Base_path}/prot1.txt")
    return (max(prot_list, key = len))


if __name__ == "__main__":
    print(find_orfs(sys.argv[1]))
