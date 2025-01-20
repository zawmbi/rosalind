'''Solved by: Linda Mansour
Date: 07/08/2024
Language: Python
ID: INI6
Problem: Dictionaries
Given: A string s of length at most 10000 letters.
Return:  The number of occurrences of each word in s, where 
words are separated by spaces. Words are case-sensitive, and
the lines in the output can be in any order.
Problem link: https://rosalind.info/problems/ini6/
'''

word_dict = {}

with open('rosalind_INI6.txt') as file:
    for line in file:
        word_set = line.split()
    for word in word_set:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

# Prints the word counts
for word, count in word_dict.items():
    print(f"{word} {count}")



