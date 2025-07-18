import sys
from Bio import SeqIO


def Correct_mut(in_file:str):
    all_seqs = []
    true_seqs =  []
    false_seqs = []
    
    for i in SeqIO.parse(in_file, "fasta"):
        all_seqs.append(i.seq)
    
    for seq in all_seqs:
        if all_seqs.count(seq) >= 2:
            true_seqs.append(str(seq))
            true_seqs.append(str(seq.reverse_complement()))
        elif str(seq) not in true_seqs and seq.reverse_complement() in all_seqs:
            true_seqs.append(str(seq))
            true_seqs.append(str(seq.reverse_complement()))
        elif str(seq) in true_seqs:
            continue
        else:
            false_seqs.append(str(seq))
    
    for f_seq in false_seqs:
        for number in range(len(f_seq)):
            temp_f_seq = f_seq
            for nucl in ["A", "C", "T", "G"]:
                temp_f_seq = temp_f_seq[:number] + nucl + temp_f_seq[number+1:]
                if temp_f_seq in true_seqs:
                    print(f"{f_seq}->{temp_f_seq}")

if __name__ == "__main__":
    Correct_mut(sys.argv[1])