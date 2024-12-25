import sys


def to_rna(in_file:str):
    with open(in_file, "r") as data:
        DNA = data.readlines()[0]
        return DNA.replace("T", "U")


if __name__ == "__main__":
    print(to_rna(sys.argv[1]))
