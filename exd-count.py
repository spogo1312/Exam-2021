#!/usr/bin/env python3

import sys

n = int(input(sys.argv))
i = 1
root = 0
while i < n:
    if n // i == i:
        root = i
        if root * root == n:
            root = i
        else:
            root = i+1
        break
    i+=1
j = 0
while j < root:
    print(j)
    j+=1