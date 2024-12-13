k=29
m=27
n=30
S=k+m+n

result=(k/S)+(m/S)*((4*k+3*m-3+2*n)/(4*S-4))+(n/S)*((2*k+m)/(2*S-2))
print(result)