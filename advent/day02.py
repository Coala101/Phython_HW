#!/usr/bin/env python
from util import read_input

reports_raw=read_input("../advent_data/day02.txt")

reports=[]
for line in reports_raw:
    for number in line:
        tmp = line.split(' ')
        tem=[]
        for num in tmp:
            int(num)
            tem.append(num)
        reports.append(tem)
#print(reports)
# reports=[
# [7,6,4,2,1],
# [1,2,7,8,9],  
# [9,7,6,2,1],
# [1,3,2,4,5],
# [8,6,4,4,1],
# [1,3,6,7,9]]
#print(reports)

def no_fluct(l):
    for number in range(len(l)-1):
        a=l[number]
        b=l[number+1]
        diff=abs(a-b)
        if diff>3:
            return False
        if diff<1:
            return False
    return True

def ascending(l):
    for number in range(len(l)-1):
        a=l[number]
        b=l[number+1]
        if a>b:
            return False
    return True
    
def descending(l):
    for number in range(len(l)-1):
        a=l[number]
        b=l[number+1]
        if a<b:
            return False
    return True 

safe=0
for l in reports:
    # if no_fluct(l)==False:
    #     continue
    if no_fluct(l)==True:
        if ascending(l)==True or descending(l)==True:
            safe+=1

print(safe)

# print(no_fluct(t))
# print(ascending(t))
# print(descending(t))
#print(safe)