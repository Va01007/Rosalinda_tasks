from Bio import SeqIO
import sys


def Calculate(in_file:str):
    seq_list = []
    res = []
    for k in SeqIO.parse(in_file, "fasta"):
        seq_list.append(f"{k.seq}")
    for i, symbol in enumerate(seq_list[0]):
        temp_s = symbol
        try:
            for next_s in seq_list[0][i+1:]:
                temp_s += next_s
                counter = 0
                for sequince in seq_list:
                    if sequince.find(temp_s) == -1:
                        break
                    else:
                        counter += 1
                    if counter == 3:
                        res.append(temp_s)
        except:
            print("ERROR")
    return sorted(res, key=len)[-1]


if __name__ == "__main__":
    print(Calculate(sys.argv[1]))
