a=4067
b=8469
result=0
for number in list(range(a, b+1)):
    if number % 2 == 1:
        result=result+number
    else:
        continue
print(result)

#result is 13802136