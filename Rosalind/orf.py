#!/usr/bin/env python

# translate an RNA sequence into protein

from util import read_input

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
    
def translate_rna_to_peptide(RNA):
    peptide=""
    start_translation = False
    for amino in range(0, len(RNA), 3):
        codon= RNA[amino:amino+3]
        
        if codon=="AUG":
            start_translation = True
            peptide=""
        if start_translation:
            if codon != "Stop":
                peptide+=code[codon]
            if codon == "Stop":
                break
            return peptide

# create a reference dictionary with the genetic code
# read the RNA in triplets
# map triplet to aminoacid

code = {
    "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
    "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
    "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
    "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
    "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
    "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
    "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}

#line_list = read_input("../rosalind_data/rosalind_prot.txt")
#rna = line_list[0]

# read the rna in triplets:
fasta = read_input('../rosalind_data/test.txt')

sequences = {}
current_id = ""
for line in fasta:
    if line[0] == ">":
        header = line
        current_id = header[1:]
        sequences[current_id] = ""
    else:
        sequence = line
        sequences[current_id] = sequences[current_id] + sequence
for id, dna in sequences.items():
    Dna=dna
    Dna_compl=""
    for nuc in Dna:
        Dna_compl+=complement(nuc)
    Dna_revcomp=Dna_compl[::-1]
    Rna=""
    Rna_compl=""
    for letter in Dna:
        if letter=="T":
            Rna+="U"
        else:
            Rna+=letter
    for letter in Dna_revcomp:
        if letter=="T":
            Rna_compl+="U"
        else:
            Rna_compl+=letter

peptide=translate_rna_to_peptide(Rna)
peptide_compl=translate_rna_to_peptide(Rna_compl)

print(peptide)
print(peptide_compl)


# for start in range(0, len(Rna), 3):
#    codon = Rna[start:start+3]
#    aminoacid = code[codon]
#    if aminoacid == "AUG":
    #    peptide = "M"
#    elif aminoacid == "Stop":
    #    break
#    else:
    #    peptide += aminoacid
  ## print(codon, "corresponds to", aminoacid)
#    print(peptide)