import sys, subprocess, os
from Bio import SeqIO


def check_quality(in_file:str):
    Base_path = os.path.dirname(os.path.realpath(__file__))
    limiter = subprocess.run(["head", "-n 1", f"{in_file}"], 
                             capture_output=True)
    with open(f"{Base_path}/temp.fastq", "w") as temp_file:
        in_temp = subprocess.run([f"tail -n +2 {in_file}"], 
                                      capture_output=True, text=True, shell=True)
        temp_file.write(in_temp.stdout)
    counter = 0
    for i in SeqIO.parse(f"{Base_path}/temp.fastq", "fastq"):
        if (sum(i.letter_annotations["phred_quality"])/len(i.letter_annotations["phred_quality"])) <= int(limiter.stdout):
            counter += 1
    os.remove(f"{Base_path}/temp.fastq")
    return counter


if __name__ == "__main__":
    print(check_quality(sys.argv[1]))
