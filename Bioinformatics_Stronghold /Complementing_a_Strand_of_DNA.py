import sys


def reverse_compliment_DNA(in_file:str):
    nucl_compliment = {"A":"T", "T":"A", "G":"C", "C":"G"}
    new_line = ""
    with open(in_file, "r") as data:
        line = data.readlines()[0]
        for symbol in line[:-1]: # Line finishes with "\n".
            new_line += nucl_compliment[symbol]
    return new_line[::-1]


if __name__ == "__main__":
    print(reverse_compliment_DNA(sys.argv[1]))
