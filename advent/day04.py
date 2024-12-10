#!/usr/bin/env python

from util import read_input

l=read_input("../advent_data/day04.txt")

# l=[
# "MMMSXXMASM",
# "MSAMXMSMSA",
# "AMXSXMAAMM",
# "MSAMASMSMX",
# "XMASAMXAMM",
# "XXAMMXXAMA",
# "SMSMSASXSS",
# "SAXAMASAAA",
# "MAMMMXMMMM",
# "MXMXAXMASX"]

def mirror(text):
    mirrored = []
    for line in text:
        mirrored.append(line[::-1])
    return mirrored

def dr_diag_starts(n):
    diag=[]
    for i in range(n):
        diag.append([i,0])
    for j in range(1, n):
        diag.append([0,j])
    return diag

def dr_diag(text, start):
    i=start[0]
    j=start[1]
    n=len(text)
    diag=""
    while j<n and i<n:
        diag+=text[i][j]
        i+=1
        j+=1
    return diag
    
l_vertical=[]
for pos in range(len(l[0])):
    #print(pos)
    new_line=""
    for line in l:
        letter=line[pos]
        new_line+=letter
    l_vertical.append(new_line)

def check_sport(text, i, j):
    upper_diagonal= text[i-1][j-1] + text[i][j]+ text[i+1][j+1]
    lower_diagonal= text[i-1][j+1] + text[i][j]+ text[i+1][j-1]
    upper=(upper_diagonal=="MAS" or upper_diagonal=="SAM")
    lower=(lower_diagonal=="MAS" or lower_diagonal=="SAM")
    if upper and lower:
        return True
    else:
        return False

# l_diagonal_left=[]
# test=""
# for pos in range(len(l[0])):
#     #print(pos)
#     for line in l:
#         letter=line[pos]
#         test+=(letter)
# print(test)
# line_len=len(l[0])

# print(l_diagonal_left)

dr_start=dr_diag_starts(len(l))
dr_diagonals=[]
for start in dr_start:
    dr_diagonals.append(dr_diag(l, start))

mirrored=mirror(l)
dl_start=dr_diag_starts(len(mirrored))
dl_diagonals=[]
for start in dl_start:
    dl_diagonals.append(dr_diag(mirrored,start))

count=0
# for row in l:
#     count+=row.count("XMAS")
#     count+=row.count("SAMX")

# for row in l_vertical:
#     count+=row.count("XMAS")
#     count+=row.count("SAMX")

# for row in dr_diagonals:
#     count+=row.count("XMAS")
#     count+=row.count("SAMX")

# for row in dl_diagonals:
#     count+=row.count("XMAS")
#     count+=row.count("SAMX")
#n=len(l)

for i in range(1, len(l)-1):
    for j in range(1, len(l)-1):
        if check_sport(l, i, j)==True:
            count+=1
# for i in range(1, len(l)-1):
#     for j in range(1, len(l[0])-1):
#         if check_sport==True:
#             count+=1

print(count)