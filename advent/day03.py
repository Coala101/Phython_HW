#!/usr/bin/env python

#s="don't()do()do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
from util import read_input

def mul(n1,n2):
    if n1==int and n2==int:
        result=n1*n2
    return result

s_raw=read_input("../advent_data/day03.txt")

s=""
for sline in s_raw:
    s+=sline

ahh=s.split("don't()")
#print(ahh)
waa=(len(ahh))
#print(waa)
z=ahh[0]
#print(ahh)

for line in ahh[1:]:
    ehh = line.split("do()")
    if len(ehh) > 1:
        for part in ehh[1:]:
            z += part

#print(z)
    
# for line in ahh:
#     if line.count("do()")==True:
#         ehh=line.split("do()")
#         #print(ehh)
#         uhh=ehh[1]
# z+=uhh

s1=z.split("mul")
# for fun in range(len(s)):
#     count=s[fun:fun+3]
#print(s1)
s2=[]
for stuff in s1:
    #print(stuff)
    if stuff[0]=="(":
        #print(stuff)
        s2.append(stuff.split(")"))
#print(s2)

papa=[]       
for thing in s2:
    #print(thing)
    lala=thing[0]
    #print(lala[-1])
    papa.append(lala.split("("))
    # if(lala[-1])=="4" or "5":
    #print(papa)
    #for lala in thing:
    #     if lala[0]=="(":
    #         print(lala)
#print(papa)

mama=[]
for thing in papa:
    lili=thing[1]
    if lili[-1]=="1" or lili[-1]=="2"or lili[-1]=="3"or lili[-1]=="4"or lili[-1]=="5"or lili[-1]=="6"or lili[-1]=="7"or lili[-1]=="8"or lili[-1]=="9"or lili[-1]=="0":
        mama.append(lili)

#print(mama)

lst=[]
#print(mama)
# for thing in mama:
#     lulu=thing.split(",")
#     for numb in lulu:
#         lolo=int(numb)
#         lst.append(lolo)
for thing in mama:
    if thing.count(",")==True:
        lulu=thing.split(",")
        for numb in lulu:
            lolo=int(numb)
            lst.append(lolo)

#print(lst)
#print(len(lst))
result=0
#print(lst)
for number in range(0, len(lst)-1, 2):
    #print(lst[number])
    #print(lst[number+1])
    result+=(lst[number]*lst[number+1])

print(result)
