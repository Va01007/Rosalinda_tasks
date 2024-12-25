import sys


def count_nucleotides(in_file:str):
    with open(in_file, "r") as data:
        line = data.readlines()[0]
        return f"{line.count('A')} {line.count('C')} {line.count('G')} {line.count('T')}"


if __name__ == "__main__":
    print(count_nucleotides(sys.argv[1]))
