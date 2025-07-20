import sys
from Bio import SeqIO


def Create_matrix(in_file:str):
    all_seqs = []
    for i in SeqIO.parse(in_file, "fasta"):
        all_seqs.append(str(i.seq))
    length_seq = len(all_seqs[0])
    result_matrix = []
    for seq in all_seqs:
        matrix_string = []
        for compare_seq in all_seqs:
            if seq == compare_seq:
                matrix_string.append(0.00000)
            else:
                overlap_counter = 0
                for number in range(length_seq):
                    if seq[number] != compare_seq[number]:
                        overlap_counter += 1
                matrix_string.append(round(overlap_counter / length_seq, 5))
        print("\t".join(map(str, matrix_string)))


if __name__ == "__main__":
    Create_matrix(sys.argv[1])
