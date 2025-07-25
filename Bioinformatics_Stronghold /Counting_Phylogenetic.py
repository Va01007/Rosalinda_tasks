import sys


def Count_P(in_file:str):
    with open(in_file, "r") as file:
        leaves = int(file.readlines()[0])
        return (leaves - 2)


if __name__ == "__main__":
    print(Count_P(sys.argv[1]))

#really strange but it s logical solve. I try in paint and everytime i has one formule
