#Strings and Lists // Hmmmmmmm am i must write commentary?
import sys


def edit_string(in_file:str):
    with open(in_file, "r") as data:
        lines = data.readlines()
        main_string = lines[0]
        borders = list(map(int, lines[1].split()))
        return (f"{main_string[borders[0]:borders[1]+1]} {main_string[borders[2]:borders[3]+1]}")


if __name__ == "__main__":
    print(edit_string(sys.argv[1]))
    