import sys


def even_string(in_file:str):
    with open(in_file, "r") as data:
        lines = data.readlines()
        for i, line in enumerate(lines):
            if i % 2 == 1: # Because indexes in a list start at zero
                print(line)


if __name__ == "__main__":
    even_string(sys.argv[1])
