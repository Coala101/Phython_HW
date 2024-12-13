#!/usr/bin/env python
from util import *
from revc import *

def check_rev_palindrome(s1):
    rev_com_s1=reverse_complement(s1)
    if s1==rev_com_s1:
        return True
    else:
        return False
    
def find_position(string, num):
    position=[]
    for pos in range(len(string)-num+1):
        count=string[pos:pos+num]
        if check_rev_palindrome(count)==True:
            position.append(pos+1)
            #position.append(len(sub_string))
    return position

def sort_by_number(item):
    return item[1]
    
#raw_string=read_input("../rosalind_data/revp_test.txt")

def main():
    fasta_dict=read_fasta("../rosalind_data/rosalind_revp.txt")

    for nr, s in fasta_dict.items():
        string=s

    #rev_string=reverse_complement(string)
        
    # print(string)
    # print(rev_string)

    ran=list(range(13))
    leng=ran[4:]
    results=[]
    for num in leng:
        found=find_position(string, num)
        if found!=[]:
            for number in found:
                results.append((number, num))
    results.sort()

    for number, num in results:
        print(number, num)
#print(find_position(string))

if __name__ == "__main__":
    main()