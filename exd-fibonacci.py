#!/usr/bin/env python3

n = int(input())
i = 0
fi = 1
last = 0
bool = False
while i < n:
    tmp = fi + last
    last = fi
    fi = tmp
    if tmp == n:
        bool = True

    i += 1
if bool == True:
    print("yes")
else:
    print("false")