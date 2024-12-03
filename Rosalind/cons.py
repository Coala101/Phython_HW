#!/usr/bin/env python

from util import *

seqs_raw=exfasta("../rosalind_data/rosalind_cons.txt")

seqs = list(seqs_raw.values())
# seqs=[
# "ATCCAGCT",
# "GGGCAACT",
# "ATGGATCT",
# "AAGCAACC",
# "TTGGAACT",
# "ATGCCATT",
# "ATGGCACT"]

profile = []
for pos in range(len(seqs[0])):
    counter={"A":0, "C":0,"G":0,"T":0}
    for sequence in seqs:
        letter=sequence[pos]
        counter[letter]+=1
    profile.append(counter)

print(profile)
seq=""
for sequence in profile:
    winner=0
    if sequence["A"]>winner:
        winner_letter="A"
        winner=sequence["A"]
    if sequence["C"]>winner:
        winner_letter="C"
        winner=sequence["C"]
    if sequence["G"]>winner:
        winner_letter="G"
        winner=sequence["G"]
    if sequence["T"]>winner:
        winner_letter="T"
        winner=sequence["T"]
    seq += winner_letter
print(seq)

for nucleotide in ["A", "C", "G", "T"]:
    counts = [str(position[nucleotide]) for position in profile]
    print(f"{nucleotide}: {' '.join(counts)}")