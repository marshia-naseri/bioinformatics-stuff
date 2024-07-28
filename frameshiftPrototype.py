# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 21:30:18 2024

@author: arshia
"""

    frameshift=False
    if len(mutated_protein)>len(protein):
        count=0
        mark=[]
        for i in range(len(mutated_protein)):
            if protein[i]!=mutated_protein[i]:
                count+=1
                mark.append(i)
            if protein[i]==mutated_protein[i]:
                count=0
            if count==5:
                frameshift=True
    if len(protein)>len(mutated_protein):
        count=0
        mark=[]
        for i in range(len(mutated_protein)):
            if protein[i]!=mutated_protein[i]:
                count+=1
                mark.append(i)
            if protein[i]==mutated_protein[i]:
                count=0
            if count==5:
                frameshift=True
    result=[frameshift, mark]   
    return result