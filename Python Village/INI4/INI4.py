'''Solved by: Linda Mansour
Date: 07/07/2024
Language: Python
ID: INI4
Problem: Conditions and Loops
Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
Problem link: https://rosalind.info/problems/ini4/
'''


with open ("rosalind_ini4.txt") as file:
    a,b = map(int, file.readline().split())

sum = 0

for i in range(a,b):
    if i % 2 == 1:
        sum += i
    

print(sum)