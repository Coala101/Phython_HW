#!/usr/bin/env python

# translate an RNA sequence into protein

from util import read_input

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

def find_orf(RNA):
    orf=[]
    for amino in range(len(RNA)-2):
        if RNA[amino:amino+3]=="AUG":
            orf.append(RNA[amino:])
    return orf

def find_orfs(rna, starts):
    """find all open reading frames in an RNA sequence"""
    orfs = []
    for start in starts:
        orf = ""
        for i in range(start, len(rna), 3):
            codon = rna[i:i+3]
            orf += codon
            if len(codon) < 3:
                break
            if code[codon] == "Stop":
                orfs.append(orf)
    return orfs

def translate_rna_to_peptide(RNA):
    peptide=""
   #start_translation = False
    for amino in range(0, len(RNA), 3):
        codon= RNA[amino:amino+3]
        aminoacid=code[codon]
       #if codon=="AUG":
           #start_translation = True
           #peptide=""
       #if start_translation:
        if aminoacid != "Stop":
            peptide+=code[codon]
        if aminoacid == "Stop":
            return peptide
        if len(codon)<3:
            break

# create a reference dictionary with the genetic code
# read the RNA in triplets
# map triplet to aminoacid

# line_list = read_input("../rosalind_data/rosalind_prot.txt")
# rna = line_list[0]

#read rna in triplets:
fasta = read_input('../rosalind_data/rosalind_orf.txt')



# rna_forward
# rna_backward
# forward_orfs = ???
# backward_orfs = ???
# for orf in all orfs: translate

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

Rna_orf=find_orf(Rna)
Rna_orf_compl=find_orf(Rna_compl)
peptide=[]
peptide_compl=[]
for dna_transcription in Rna_orf:
    pep=translate_rna_to_peptide(dna_transcription)
    peptide.append(pep)
for dna_transciption_compl in Rna_orf_compl:
    pep_compl=translate_rna_to_peptide(dna_transciption_compl)
    peptide.append(pep_compl)
for pep in peptide:
    print(pep)
for pep in peptide_compl:
    print(pep)


# for start in range(0, len(Rna), 3):
#    codon = Rna[start:start+3]
#    aminoacid = code[codon]
#    if aminoacid == "AUG":
#        peptide = "M"
#    elif aminoacid == "Stop":
#        break
#    else:
#        peptide += aminoacid
#   # print(codon, "corresponds to", aminoacid)
#    print(peptide)