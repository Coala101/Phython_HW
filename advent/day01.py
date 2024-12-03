#!/usr/bin/env python

# chief historian's office; comparing reports
from util import read_input

def count_occurrences(x, l):
    #function that counts occurances of number x in list l
    counter=0
    for number in l:
        if x==number:
            counter+=1
    return counter
# first, read the raw data
raw = read_input("../advent_data/day01.txt")
list_a = []
list_b = []
for line in raw:
    tmp = line.split(' ')
    a = int(tmp[0])
    b = int(tmp[-1])
    list_a.append(a)
    list_b.append(b)

#print(list_a)
# print(list_b)

# now we need to sort the lists
list_a.sort()
list_b.sort()
#print(list_a)

# calculate differences!
sum_of_differences = 0
for a, b in zip(list_a, list_b):
    diff = abs(a - b)
    sum_of_differences += diff

#print(sum_of_differences)
result=0
for number in list_a:
    result+=number*count_occurrences(number, list_b)

print(result)