'''Solved by: Linda Mansour
Date: 07/07/2024
Language: Python
ID: INI5
Problem: Working with Files
Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file.
Assume 1-based numbering of lines.
Problem link: https://rosalind.info/problems/ini5/
'''


count = 0
new_file = open('new_file.txt','w')

with open('rosalind_INI5.txt') as file:
    for line in file:
        count+=1
        if count % 2 == 0:
            new_file.write(str(line))
            print(line, end='')

