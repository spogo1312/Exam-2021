#!/usr/bin/env python3

n = int(input())
s = []
s.append("|")
i = 0
while i < n:
    s.append(" ")
    
    i += 1
j = 0
while j <= n:  # Im not sure how he wants us to determine
    j = int(input())  # what is the last input
    if j < n:
        s[j+1] = "*"  # so i just said whenever input is
    #larger than the first number
    #if you know the intended way let me know
s.append("|")
str = ""            #this piece of code is just to convert from list
for element in s:   # to string 
    str += element  # I think the correct solution is not to use 
print(str)          #list at all