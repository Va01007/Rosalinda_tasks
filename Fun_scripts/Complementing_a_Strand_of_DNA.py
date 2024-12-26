import sys


def reverse_compliment_DNA(in_file:str):
    with open(in_file, "r") as data:
        line = data.readlines()[0][:-1]
        line = line.replace("T", "!")
        line = line.replace("A", "T")
        line = line.replace("!", "A")
        line = line.replace("G", "!")
        line = line.replace("C", "G")
        line = line.replace("!", "C")
    return line[::-1]


if __name__ == "__main__":
    print(reverse_compliment_DNA(sys.argv[1]))


#I think it is not beautiful solve
#But i love it