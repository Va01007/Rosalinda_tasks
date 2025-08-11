from Bio.Seq import translate
import sys


def prot_translate(in_file:str):
    with open(in_file, "r") as file:
        lines = file.readlines()
        seq = lines[0].rstrip()
        prot = lines[1].rstrip()
        for i in range(1, 34):
            try:
                if prot == translate(seq, table = i, to_stop=True):
                    return i
            except:
                pass


if __name__ == "__main__":
    print(prot_translate(sys.argv[1]))
