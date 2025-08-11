import sys, subprocess, os
from Bio import SeqIO
from Bio import Entrez


def global_aligment(in_file:str):
    Base_path = os.path.dirname(os.path.realpath(__file__))
    with open(in_file, "r") as file:
        args = " ".join(file.readlines()).split()
        seq_list = []
        handle = Entrez.efetch(db="nucleotide", id=args, rettype="fasta")
        for i in SeqIO.parse(handle, "fasta"):
            seq_list.append(str(i.seq))
        with open(f"{Base_path}/A_temp_seq.txt", "w") as TMP1:
            TMP1.write(seq_list[0])
        with open(f"{Base_path}/B_temp_seq.txt", "w") as TMP2:
            TMP2.write(seq_list[1])
        subprocess.run([f"stretcher -asequence {Base_path}/A_temp_seq.txt -bsequence {Base_path}/B_temp_seq.txt -gapopen 10 -gapextend 1 -outfile {Base_path}/bezdna.txt"], 
                                      capture_output=True, text=True, shell=True)
        with open(f"{Base_path}/bezdna.txt", "r") as check:
            lines = check.readlines()
            for line in lines:
                if line.startswith("# Score:"):
                    result = ((line.split())[2])
                    break
    os.remove(f"{Base_path}/bezdna.txt")
    os.remove(f"{Base_path}/A_temp_seq.txt")
    os.remove(f"{Base_path}/B_temp_seq.txt")
    return result


if __name__ == "__main__":
    print(global_aligment(sys.argv[1]))

