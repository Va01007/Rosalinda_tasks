import sys


def convert_toFasta(in_file:str):
    with open(in_file, "r") as file:
        lines = file.readlines()
        for number, line in enumerate(lines):
            if number % 4 == 0:
                print(f">{lines[number][1:]}{lines[(number+ 1)][:-1]}")

if __name__ == "__main__":
    convert_toFasta(sys.argv[1])

#just a logical solution
