'''
Solved by: Linda Mansour
Date: 04/03/2024
Language: Python
ID: RNA
Problem: Transcribing DNA into RNA
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u
is formed by replacing all occurrences of 'T' in t with 'U' in u.
Problem link: https://rosalind.info/problems/rna/
'''

with open("rosalind_rna.txt") as file:
    t = file.readline().strip()
    
t = t.replace('T','U')
print(t)

# Correct Output: 
#UUGAUCGAGGUGGAUAACUUACGUAGCACUUUUGACUCCCACUGUUACAUUUCACCACUAGCGACUUCUGAAUCCGAAAACGUUAAGAGUUACAAAUCUAGGCCGGAGCGCGUCACCCACACAUCACGGAUUUAUCUGCGCUGUCAAUUCUAUCAGAUACAGAAUGUUAUGCAAAGGGUUGUAUUUUGUUAUCUAUUUGAAUCGGGCUGCGCAGCUCAUGUCGACUUAUGUCCACAUCAGUUUAUCCCUGUGCUGUGAAGGUCACUAAUCGAUGUCGAACAAUAUCCUUGAGACAUCAGGCACCGAAUCUGCCCUAGUCUAUCUUAGCACUAAUUUUAAGUCUUCUAGACGUCCUACUUAACCUUUUAGUGCAGUAAGCGGGGACAACUAGCAUUUAGCGACACGAUACGUCGUAUGCGCGCUAAAAAUGAACGUGAAGAAGGUAACGCGCACCCGCAGGUGCCCACCAAUGCAAUCGCCUGUAAGCGGAACAACUUCUAGAAACCUUCUGUGUUAAGAAUUUCAGCGUUGACUAGAAGUUCAUCGGGUGGCUCAAGAUUUCCCCACCGUUGACCUCUAAAUCCUGUCGGACUUAUGGAUCAUGGUGUAGGAUGACUUACAGGCGGUGAAGGUUCGCGAUCCACACCAGCGAGUUGCUGAUUACUUAAAGUUUAGCGGCCAGUAACUUCACGCACUAGUAGCUUAAUAUCCGACGAUCAGUUUCAAAGUUCUCAUUCCUAAACCGCGCUUGGGGUGUCCUCUCCCGUCAUGUCCUACAGAGCUUUCUUGCUGAAUUAAACGAAGCCAAGGAUGGUUAACUACACGGUCCGCCCAGUUACCCUUUGGUUUCCGGAGUUUACCGAGAAUGCCUUUUCAUAGUCACGCCAAACAGAGCCCCUGGAUCUCUCCCUAUCCGGGAGAUUUAAGGGUGCCUCCAACUGGGUUAUGAUCUCUC