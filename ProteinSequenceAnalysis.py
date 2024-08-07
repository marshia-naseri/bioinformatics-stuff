# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:30:28 2024

@author: arshia
"""

allaa={'A': {'n': 0, 'weight': 71.0788, 'formula': {'C': 3, 'H': 7, 'O': 2, 'N': 1}},
       'R': {'n': 0, 'weight': 156.1875, 'formula': {'C': 6, 'H': 14, 'O': 2, 'N': 4}},
       'N': {'n': 0, 'weight': 114.1038, 'formula': {'C': 4, 'H': 8, 'O':3, 'N': 2}},
       'D': {'n': 0, 'weight': 115.0886, 'formula': {'C': 4, 'H': 7, 'O': 4, 'N': 1}},
       'C': {'n': 0, 'weight': 103.1388, 'formula': {'C': 3, 'H': 7, 'O': 2, 'N': 1, 'S': 1}},
       'E': {'n': 0, 'weight': 129.1155, 'formula': {'C': 5, 'H': 9, 'O': 4, 'N': 1}},
       'Q': {'n': 0, 'weight': 128.1307, 'formula': {'C': 5, 'H': 10, 'O': 3, 'N': 2}},
       'G': {'n': 0, 'weight': 57.0519, 'formula': {'C': 2, 'H': 5, 'O': 2, 'N': 1}},
       'H': {'n': 0, 'weight': 137.1411, 'formula': {'C': 6, 'H': 9, 'O': 2, 'N': 3}},
       'I': {'n': 0, 'weight': 113.1594, 'formula': {'C': 6, 'H': 13, 'O': 2, 'N': 1}},
       'L': {'n': 0, 'weight': 113.1594, 'formula': {'C': 6, 'H': 13, 'O': 2, 'N': 1}},
       'K': {'n': 0, 'weight': 128.1741, 'formula': {'C': 6, 'H': 14, 'O': 2, 'N': 2}},
       'M': {'n': 0, 'weight': 131.1926, 'formula': {'C': 5, 'H': 11, 'O': 2, 'N': 1, 'S': 1}},
       'F': {'n': 0, 'weight': 147.1766, 'formula': {'C': 9, 'H': 11, 'O': 2, 'N': 1}},
       'P': {'n': 0, 'weight': 97.1167, 'formula': {'C': 5, 'H': 9, 'O': 2, 'N': 1}},
       'S': {'n': 0, 'weight': 87.0782, 'formula': {'C': 3, 'H': 7, 'O': 3, 'N': 1}},
       'T': {'n': 0, 'weight': 101.1051, 'formula': {'C': 4, 'H': 9, 'O': 3, 'N': 1}},
       'W': {'n': 0, 'weight': 186.2132, 'formula': {'C': 11, 'H': 12, 'O': 2, 'N': 2}},
       'Y': {'n': 0, 'weight': 163.1760, 'formula': {'C': 9, 'H': 11, 'O': 3, 'N': 1}},
       'V': {'n': 0, 'weight': 99.1326, 'formula': {'C': 5, 'H': 11, 'O': 2, 'N': 1}}}

#bcl-2= MAQAGRTGYDNREIVMKYIHYKLSQRGYEWDVGDVDAAPLGAAPTPGIFSFQPESNPTPAVHRDMAARTSPLRPIVATTGPTLSPVPPVVHLTLRRAGDDFSRRYRRDFAEMSSQLHLTPFTARGRFATVVEELFRDGVNWGRIVAFFEFGGVMCVESVNREMSPLVDNIALWMTEYLNRHLHTWIQDNGGWDAFVELYGPSVRPLFDFSWLSLKTLLSLALVGACITLGTYLGHK

p=input('Please enter your protein sequence= ')
p=''.join(p.splitlines()).strip()

wsum=0
n=0
ft={}
for aa in p:
    n+=1
    allaa[aa]['n']+=1
    f=allaa[aa].get('formula')
    for m in f:
        ft.setdefault(m,0)
        ft[m]+=f[m]
    wsum+=allaa.get(aa).get('weight')
print('------------------------\nResults:\n\nProtein weight=', wsum , 'Da\n\nAmino-Acid percentages:')
for i,j in allaa.items():
    aap=j.get('n')/n*100
    print(i,'=', aap, '%')
print('Protein formula: ')
fp=''
for m,n in ft.items():
    fp+=m+str(n)+','
print(fp)