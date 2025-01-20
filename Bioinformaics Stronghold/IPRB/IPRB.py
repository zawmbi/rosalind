'''
Solved by: Linda Mansour
Date: 10/16/2024
Language: Python
ID: IPRB
Problem: Mendel's First Law

Given: Three positive integers k, m, and n, representing a population
containing k+m+n organisms: k individuals are homozygous dominant for
a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will 
produce an individual possessing a dominant allele (and thus displaying 
the dominant phenotype). Assume that any two organisms can mate.
Problem link: https://rosalind.info/problems/ipbr/
'''

with open("rosalind_iprb.txt") as file:
    k, m, n = map(int, file.readline().split())

    
file.close()
total = k + m + n # total number of alleles

# The probability that two randomly selected mating organisms will 
# produce an individual possessing a dominant allele

# aka ONE parent needs to be either k or m, not both. 

# probability for m or k is both 2/6. (4/6) for the parents to be either.

# p for both parents dom allele: 0.6667 ? I think (4/6) +  (4/6)

# p for 1st parent:  

probability = (2/6) * (2/6) 
print(probability)