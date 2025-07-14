import sys


def Count_tree(in_file:str):
    with open(in_file, "r") as file:
        lines = file.readlines()
    S = int(lines[0])
    K = len(lines)
    return (S - K)


if __name__ == "__main__":
    print(Count_tree(sys.argv[1]))
#LOL
