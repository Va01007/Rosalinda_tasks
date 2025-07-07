import sys
from Bio import SeqIO


def Show_frames(in_file:str, acid_dict:dict):
    for sequince in SeqIO.parse(in_file, "fasta"):
        forward_seq = sequince
        reverse_seq = sequince.reverse_complement()
        list_prot = []
        for i, nucl in enumerate(forward_seq.seq):
            if forward_seq.seq[i:i+3] == "ATG":
                temp = ""
                for k in range(i, len(forward_seq.seq), 3):
                    if forward_seq.seq[k:k+3] == "TGA" or forward_seq.seq[k:k+3] == "TAA" or forward_seq.seq[k:k+3] == "TAG":
                        list_prot.append(temp)
                        break
                    else:
                        try:
                            temp += Acids[forward_seq.seq[k:k+3]]
                        except:
                            break
                            
        for n, nuclr in enumerate(reverse_seq.seq):
            if reverse_seq.seq[n:n+3] == "ATG":
                tempr = ""
                for d in range(n, len(reverse_seq.seq), 3):
                    if reverse_seq.seq[d:d+3] == "TGA" or reverse_seq.seq[d:d+3] == "TAA" or reverse_seq.seq[d:d+3] == "TAG":
                        list_prot.append(tempr)
                        break
                    else:
                        try:
                            tempr += Acids[reverse_seq.seq[d:d+3]]
                        except:
                            break
    return set(list_prot)


if __name__ == "__main__":
    Acids = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L", "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "TAT":"Y", "TAC":"Y", "TAA":"!", "TAG":"!", \
"TGT":"C", "TGC":"C", "TGA":"!", "TGG":"W", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L", "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P", \
"CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M", \
"ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R", \
"GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E", \
"GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    [print(prot) for prot in Show_frames(sys.argv[1], Acids)]
