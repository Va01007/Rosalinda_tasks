#bioinformatics stronghold Consensus and Profile // pizdec
f = open("/STORAGE_MG/avasilev/Not_for_Alexey/Rosalind_projects/rosalind_cons.txt", mode="r")
w = open("/STORAGE_MG/avasilev/Not_for_Alexey/Rosalind_projects/out.txt", mode="w")
lines = f.readlines()
Reestr = {}
Nuc = {}
final = ""
Aden = ""
Guan = ""
Cito = ""
Timi = ""
temp = ""
bag = []
i = 0
for line in lines:
    i += 1
    if line[0] == ">":
        Cum = []
        for strings in lines[i:]:
            if strings[0] == ">" or strings == "":
                temp = "".join(Cum)
                Length = int(len(temp))
                #print(Length)
                Reestr[line.rstrip("\n")[1:]] = temp
                break
            else:
                Cum.append(strings.rstrip("\n"))
        temp = "".join(Cum)
        Reestr[line.rstrip("\n")[1:]] = temp
for d in range(Length): # fiiling dictionar
    Nuc[f"A{d}"] = 0
    Nuc[f"T{d}"] = 0
    Nuc[f"G{d}"] = 0
    Nuc[f"C{d}"] = 0
for k, n in enumerate(Reestr):
    for g in range(Length):
        #print(g)
        if (Reestr[n])[g] == "A":
            Nuc[f"A{g}"] += 1
        elif (Reestr[n])[g] == "T":
            Nuc[f"T{g}"] += 1
        elif (Reestr[n])[g] == "G":
            Nuc[f"G{g}"] += 1
        elif (Reestr[n])[g] == "C":
            Nuc[f"C{g}"] += 1
for m in range(Length):
    Aden += f"{Nuc[f'A{m}']} "
    Cito += f"{Nuc[f'C{m}']} "
    Guan += f"{Nuc[f'G{m}']} "
    Timi += f"{Nuc[f'T{m}']} "
for j in range(Length):
    if Nuc[f"A{j}"] >= Nuc[f"T{j}"] and Nuc[f"A{j}"] >= Nuc[f"G{j}"] and Nuc[f"A{j}"] >= Nuc[f"C{j}"]:
        Nuc.pop(f"T{j}")
        Nuc.pop(f"G{j}")
        Nuc.pop(f"C{j}")
    elif Nuc[f"T{j}"] >= Nuc[f"A{j}"] and Nuc[f"T{j}"] >= Nuc[f"G{j}"] and Nuc[f"T{j}"] >= Nuc[f"C{j}"]:
        Nuc.pop(f"A{j}")
        Nuc.pop(f"G{j}")
        Nuc.pop(f"C{j}")
    elif Nuc[f"G{j}"] >= Nuc[f"T{j}"] and Nuc[f"G{j}"] >= Nuc[f"A{j}"] and Nuc[f"G{j}"] >= Nuc[f"C{j}"]:
        Nuc.pop(f"T{j}")
        Nuc.pop(f"A{j}")
        Nuc.pop(f"C{j}")
    elif Nuc[f"C{j}"] >= Nuc[f"A{j}"] and Nuc[f"C{j}"] >= Nuc[f"G{j}"] and Nuc[f"C{j}"] >= Nuc[f"T{j}"]:
        Nuc.pop(f"T{j}")
        Nuc.pop(f"G{j}")
        Nuc.pop(f"A{j}")
for obj in Nuc:
    final += obj[0]
w.write(final+"\n")
w.write(f"A: "+Aden+"\n")
w.write(f"C: "+Cito+"\n")
w.write(f"G: "+Guan+"\n")
w.write(f"T: "+Timi+"\n")
f.close()
w.close()

#my first try and i think it was a veeeeeery long and silly script