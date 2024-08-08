# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:08:20 2024

@author: arshia
"""

#dictionary for each codon, and its count
codons={'ttt': ['F', 0], 'ttc': ['F', 0], 
        'tta': ['L', 0], 'ttg': ['L', 0], 'ctt': ['L', 0], 'ctc': ['L', 0], 'cta': ['L', 0], 'ctg': ['L', 0], 
        'tct': ['S', 0], 'tcc': ['S', 0], 'tca': ['L', 0], 'tcg': ['S', 0], 'agt': ['S', 0], 'agc': ['S', 0], 
        'tat': ['Y', 0], 'tac': ['Y', 0], 
        'tgt': ['C', 0], 'tgc': ['C', 0], 
        'tgg': ['W', 0], 
        'cct': ['P', 0], 'ccc': ['P', 0], 'cca': ['P', 0], 'ccg': ['P', 0], 
        'cat': ['H', 0], 'cac': ['H', 0], 
        'caa': ['Q', 0], 'cag': ['Q', 0], 
        'cgt': ['R', 0], 'cgc': ['R', 0], 'cga': ['R', 0], 'cgg': ['R', 0], 'aga': ['R', 0], 'agg': ['R', 0], 
        'att': ['I', 0], 'atc': ['I', 0], 'ata': ['I', 0], 
        'atg': ['M', 0], 
        'act': ['T', 0], 'acc': ['T', 0], 'aca': ['T', 0], 'acg': ['T', 0], 
        'aat': ['N', 0], 'aac': ['N', 0], 
        'aaa': ['K', 0], 'aag': ['K', 0], 
        'gtt': ['V', 0], 'gtc': ['V', 0], 'gta': ['V', 0], 'gtg': ['V', 0], 
        'gct': ['A', 0], 'gcc': ['A', 0], 'gca': ['A', 0], 'gcg': ['A', 0], 
        'gat': ['D', 0], 'gac': ['D', 0], 
        'gaa': ['E', 0], 'gag': ['E', 0], 
        'ggt': ['G', 0], 'ggc': ['G', 0], 'gga': ['G', 0], 'ggg': ['G', 0]
        }
end=['taa','tag','tga']

dna=input('please enter your dna sequence: ')
dna=''.join(dna.splitlines()).strip()
p=''
n=0
print('\nresults:\n')
while len(dna)>=3:
    codon=dna[0:3]
    n+=1
    if codon in end:
        scodon=codon
        break
    x=codons.get(codon)
    p+=x[0]
    x[1]+=1
    codons[codon]=x
    dna=dna[3:]
m=''
l=''
for codon in codons:
    x=codons.get(codon)
    pc=x[1]/n*100
    if pc!=0:
        print(f"{codon} : {pc}%")
    if m=='':
        m=x[1]
        ms=codon
    else:
        if x[1]>m:
            m=x[1]
            ms=codon
    if l=='':
        l=x[1]
        ls=codon
    else:
        if x[1]<l and x[1]!=0:
            l=x[1]
            ls=codon
    if l==0:
        l=''
    if m==0:
        m=''
print(f"{scodon} : {1/n*100}%")
print(f"\nmax : {ms},{m}\nleast : {ls},{l}")
print(f"protein : {p}")
        