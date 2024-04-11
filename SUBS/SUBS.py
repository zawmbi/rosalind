'''
Solved by: Linda Mansour
Date: 04/11/2024
Language: Python
ID: SUBS
Problem:  Finding a Motif in DNA
Given two strings s and t, t is a substring of s if t
is contained as a contiguous collection of symbols in s
(as a result, t must be no longer than s).

The position of a symbol in a string is the total number 
of symbols found to its left, including itself (e.g., the 
positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG"
are 2, 5, 6, 15, 17, and 18). The symbol at position i of s
is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k
represent the starting and ending positions of the substring 
in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", 
then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j;
note that t will have multiple locations in s if it occurs 
more than once as a substring of s.

Problem link: https://rosalind.info/problems/subs/
'''

# with open ("rosalind_subs.txt") as file:
#     s = file.readline().strip()
#     t = file.readline().strip()

s = "GATATATGCATATACTT"
t = "ATAT"

    
print(s)
print(t)


for i in s:
    if t in s:
        print(i)
