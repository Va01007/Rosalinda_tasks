import sys


def find_motif(in_file:str):
    with open(in_file, "r") as data:
        lines = data.readlines()
        DNA = lines[0].rstrip("\n")
        motif = lines[1].rstrip("\n")
        result_list = []
        
        for i in range(len(DNA)):
            if DNA[i:(i+len(motif))] == motif:
                result_list.append(i+1)
        return " ".join(map(str, result_list))


if __name__ == "__main__":
    print(find_motif(sys.argv[1]))
