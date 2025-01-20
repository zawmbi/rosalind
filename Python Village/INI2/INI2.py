'''Solved by: Linda Mansour
Date: 04/12/2024
Language: Python
ID: INI2
Problem: Variables and Some Arithmetic
Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the
hypotenuse of the right triangle whose legs have lengths a and b.
Problem link: https://rosalind.info/problems/ini1/
'''
import math

with open ("rosalind_ini2.txt", 'r') as file:
    a, b = map(int, file.readline().split())

c = math.pow(a,2) + math.pow(b,2)

print(c)

# Correct output:
# 1792485