import sys, subprocess, os
from Bio import SeqIO


def Local_aligment(in_file:str):
    Base_path = os.path.dirname(os.path.realpath(__file__))
    result = subprocess.run([f"clustalo -i {in_file} > {Base_path}/temp_fasta.fasta"], 
                                      capture_output=False, text=False, shell=True)
    seq_list = []
    id_dict = {}
    for i in SeqIO.parse(f"{Base_path}/temp_fasta.fasta", "fasta"):
        seq_list.append(str(i.seq))
        id_dict[str(i.seq)] = str(i.id)
    res = {k:[] for k in seq_list}
    for seq in seq_list:
        for nucl in range(0, len(seq)):
            temp_counter = 0
            for num in range(0, len(seq_list)):
                if seq[nucl] == seq_list[num][nucl]:
                    temp_counter += 1
            res[seq].append(temp_counter)
        res[seq] = sum(res[seq]) / len(res[seq])
    os.remove(f"{Base_path}/temp_fasta.fasta")
    return (id_dict[min(res, key=res.get)])


if __name__ == "__main__":
    print(Local_aligment(sys.argv[1]))

