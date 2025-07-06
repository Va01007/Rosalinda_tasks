import sys


def Count_percentage(in_file:str):
    with open(in_file, "r") as file:
        lines = file.readlines()[0].split()
    bag = []
    breeds = 0
    count = 0
    for domi, i in enumerate(range(int(lines[0]))):
        bag.append(f"{i}D")
    for gete, i in enumerate(range(int(lines[1]))):
        bag.append(f"{i}G")
    for rece, i in enumerate(range(int(lines[2]))):
        bag.append(f"{i}R")
    for gen1 in bag:
        if gen1.find("D") > 0:
            for gen2 in bag:
                if gen2.find("D") > 0 and gen2 != gen1:
                    count += 100
                    breeds += 1
                elif gen2.find("G") > 0:
                    count += 100
                    breeds += 1
                elif gen2.find("R") > 0:
                    count += 100
                    breeds += 1
        elif gen1.find("G") > 0:
            for gen2 in bag:
                if gen2.find("D") > 0:
                    count += 100
                    breeds += 1
                elif gen2.find("G") > 0 and gen2 != gen1:
                    count += 75
                    breeds += 1
                elif gen2.find("R") > 0:
                    count += 50
                    breeds += 1
        elif gen1.find("R") > 0:
            for gen2 in bag:
                if gen2.find("D") > 0:
                    count += 100
                    breeds += 1
                elif gen2.find("G") > 0:
                    count += 50
                    breeds += 1
                elif gen2.find("R") > 0  and gen2 != gen1:
                    count += 0
                    breeds += 1
    return (round(((count/breeds)/100), 5))


if __name__ == "__main__":
    print(Count_percentage(sys.argv[1]))

#Yep, i know that its not very smart solution. I will change it after some time