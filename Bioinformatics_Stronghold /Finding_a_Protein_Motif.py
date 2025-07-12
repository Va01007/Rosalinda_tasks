import requests
import sys


def Prot_motif(in_file:str):
    res = {}
    with open(in_file, "r") as start_file:
        for line in start_file.readlines():
            res[line[:-1]] = []
            with requests.get(f"http://www.uniprot.org/uniprot/{line[0:6]}.fasta") as file: # just fix old data names
                main_line = (str(file.content)).split()[-1]
                main_line = "".join(main_line.split("\\n")[1:-1])
                for i, bukva in enumerate(main_line):
                    try:
                        if main_line[i] == "N" and main_line[i+1] != "P" and (main_line[i+2] == "S" or main_line[i+2] == "T") and main_line[i+3] != "P":
                            res[line[:-1]].append(i+1)
                    except:
                        pass
    for i in res.keys():
        if res[i] == []:
            continue
        else:
            print(i)
            print("\t".join(map(str, res[i])))


if __name__ == "__main__":
    Prot_motif(sys.argv[1])


#When I tried this script on several datasets, I encountered some issues. Maybe some IDs are broken, or there's another problem.