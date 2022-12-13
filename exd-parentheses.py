#!/usr/bin/env python3

with open("C:\\Users\\podha\\OneDrive\\Dokumenty\\Exam2021\\Exam-2021\\test.txt") as f: #here inside open function you 
    #need to change your for the code to work on your machine
    #the path is the path where is your test.txt file located
    chars = f.read()
new_line = True
i = 0
s = ""
while i < len(chars):
    if chars[i] == "(" and new_line:
        i += 1
        while chars[i] != ")":
            s = s + chars[i]
            i += 1
        new_line = False
        #s = s + "\n"           # \n is a new line character
        print(s)
        s = ""
    if chars[i] == "\n":
        new_line = True
    i += 1

#print(s[:-1]) #the [:-1] prints the string without the last character because i add \n at the end of every perentheses 