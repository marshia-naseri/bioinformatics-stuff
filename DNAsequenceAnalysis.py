# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:30:55 2024

@author: arshia
"""

def gc_percentage(dna):
    g=dna.count('G')
    c=dna.count('C')
    gc=(g+c)/len(dna)*100
    return gc

def r_complement(dna):
    rdna=dna[-1::-1]
    cdna=[]
    for n in rdna:
        if n=='A':
            cdna.append('T')
        elif n=='T':
            cdna.append('A')
        elif n=='G':
            cdna.append('C')
        elif n=='C':
            cdna.append('G')
        else:
            cdna.append('-')
    cdna=''.join(cdna)
    return cdna

def find_rlfp(dna):
    rtotal=[]
    rsite=input('enter intened restriction enzyme site: ')
    rl=len(rsite)
    for i in range(0,len(dna)-rl):
        x=dna[i:i+rl]
        if x==rsite:
            rtotal.append(i+1)
    if rtotal==[]:
        rtotal='no sites found!'
    return rtotal

dna=input('please enter your strand on dna: ')
while 1==1:
    print('\n1) determine G/C percentage\n2) find the reverse compliment\n3) find all intended restriction enzyme sites\n4) quit program\n')
    n=input('what do you wish to do: ')
    if n=='1':
        gc=gc_percentage(dna)
        print(F"G/C percentage={gc}%")
    if n=='2':
        r=r_complement(dna)
        print(f"the reverse complement is: {r}")
    if n=='3':
        rlfp=find_rlfp(dna)
        print(f"found locations are: {rlfp}")
    if n=='4':
        print('program closing...')
        break
    else:
        print('invalid input!')