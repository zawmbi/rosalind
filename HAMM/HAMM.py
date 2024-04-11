'''
Solved by: Linda Mansour
Date: 04/07/2024
Language: Python
ID: HAMM
Problem: Counting Point Mutations
Given two strings s and t of equal length, the
Hamming distance between s and t, denoted dH(s,t), is
the number of corresponding symbols that differ in s and t.
'''

with open("rosalind_hamm.txt") as file:
    s = file.readline().strip()
    t = file.readline().strip()


# s = str("GAGCCTACTAACGGGAT")
# t = str("CATCGTAATGACGGCCT")

hamming = 0

for base in range(len(s)):
    if (s[base] != t[base]):
        hamming+=1

print(hamming)

# Correct Output:
# 464