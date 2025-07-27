import sys
from Bio.Seq import Seq


def count_nucl(in_file:str):
    with open(in_file, "r") as file:
        line = Seq(file.readlines()[0])
    return (f'{line.count("A")} {line.count("C")} {line.count("G")} {line.count("T")}')


if __name__ == "__main__":
    print(count_nucl(sys.argv[1]))

# SMS 2 usage instructions for sequence analysis task:
# 1. Download the package from GitHub:
#    https://github.com/paulstothard/sequence_manipulation_suite
# 2. For DNA analysis:
#    - Copy your DNA sequence
#    - Open DNA_stats.html from local package
#    - Or use web version:
#      https://www.bioinformatics.org/sms2/dna_stats.html
# Note: Works with both local installation and online version
