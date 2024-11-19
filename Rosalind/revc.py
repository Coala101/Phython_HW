def complement(letter):
    if letter=="A":
        return "T"
    elif letter=="C":
        return "G"
    elif letter=="G":
        return "C"
    elif letter=="T":
        return "A"
    else:
        return "N"
    
Dna=""
Dna_compl=""
for nuc in Dna:
    Dna_compl+=complement(nuc)

Dna_compl[::-1]

#for letter in Dna:
#    if letter=="A":
#        Dna_compl+="T"
#    elif letter=="C":
#        Dna_compl+="G"
#    elif letter=="G":
#        Dna_compl+="C"
#    elif letter=="T":
#        Dna_compl+="A"