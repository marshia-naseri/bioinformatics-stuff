# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:27:22 2024

@author: arshia
"""
allspecies={'Homosapien':{
        'F': [['ttt', 'ttc'], [0.45, 0.55]],
        'L': [['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'], [0.07, 0.13, 0.13, 0.20, 0.07, 0.41]],
        'Y': [['tat', 'tac'], [0.43, 0.57]],
        'H': [['cat', 'cac'], [0.41, 0.59]],
        'Q': [['caa', 'cag'], [0.25, 0.75]],
        'I': [['att', 'atc', 'ata'], [0.36, 0.48, 0.16]],
        'M': [['atg'], [1.00]],
        'N': [['aat', 'aac'], [0.46, 0.54]],
        'K': [['aaa', 'aag'], [0.42, 0.58]],
        'V': [['gtt', 'gtc', 'gta', 'gtg'], [0.18, 0.24, 0.11, 0.47]],
        'D': [['gat', 'gac'], [0.46, 0.54]],
        'E': [['gaa', 'gag'], [0.42, 0.58]],
        'S': [['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'], [0.18, 0.22, 0.15, 0.06, 0.14, 0.24]],
        'C': [['tgt', 'tgc'], [0.45, 0.55]], 
        'W': [['tgg'], [1.00]], 
        'P': [['cct', 'ccc', 'cca', 'ccg'], [0.28, 0.33, 0.27, 0.11]],
        'R': [['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg'], [0.08, 0.19, 0.11, 0.21, 0.20, 0.20]], 
        'T': [['act', 'acc', 'aca', 'acg'], [0.24, 0.36, 0.28, 0.12]],
        'A': [['gct', 'gcc', 'gca', 'gcg'], [0.26, 0.40, 0.23, 0.11]], 
        'G': [['ggt', 'ggc', 'gga', 'ggg'], [0.16, 0.34, 0.25, 0.25]], 
        'end': [['taa', 'tag', 'tga'], [0.28, 0.20, 0.52]]}, 
    'E. coli': {
        'F': [['ttt', 'ttc'], [0.58, 0.42]],
        'L': [['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'], [0.14, 0.13, 0.12, 0.10, 0.04, 0.47]],
        'Y': [['tat', 'tac'], [0.59, 0.41]], 
        'H': [['cat', 'cac'], [0.57, 0.43]],
        'Q': [['caa', 'cag'], [0.34, 0.66]],  
        'I': [['att', 'atc', 'ata'], [0.49, 0.39, 0.11]],
        'M': [['atg'], [1.00]],
        'N': [['aat', 'aac'], [0.49, 0.51]],
        'K': [['aaa', 'aag'], [0.74, 0.26]],
        'V': [['gtt', 'gtc', 'gta', 'gtg'], [0.28, 0.20, 0.17, 0.35]],
        'D': [['gat', 'gac'], [0.63, 0.37]],
        'E': [['gaa', 'gag'], [0.68, 0.32]],
        'S': [['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'], [0.17, 0.15, 0.14, 0.14, 0.16, 0.25]],
        'C': [['tgt', 'tgc'], [0.46, 0.54]],  
        'W': [['tgg'], [1.00]], 
        'P': [['cct', 'ccc', 'cca', 'ccg'], [0.18, 0.13, 0.20, 0.49]], 
        'R': [['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg'], [0.36, 0.35, 0.08, 0.11, 0.07, 0.04]], 
        'T': [['act', 'acc', 'aca', 'acg'], [0.19, 0.40, 0.17, 0.25]],  
        'A': [['gct', 'gcc', 'gca', 'gcg'], [0.18, 0.26, 0.23, 0.33]], 
        'G': [['ggt', 'ggc', 'gga', 'ggg'], [0.35, 0.37, 0.13, 0.15]],  
        'end': [['taa', 'tag', 'tga'], [0.61, 0.09, 0.30]]},
    'Yeast': {
        'F': [['ttt', 'ttc'], [0.59, 0.41]],
        'L': [['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'], [0.28, 0.29, 0.13, 0.06, 0.14, 0.11]],
        'Y': [['tat', 'tac'], [0.56, 0.44]], 
        'H': [['cat', 'cac'], [0.64, 0.36]],
        'Q': [['caa', 'cag'], [0.69, 0.31]], 
        'I': [['att', 'atc', 'ata'], [0.46, 0.26, 0.27]],
        'M': [['atg'], [1.00]],
        'N': [['aat', 'aac'], [0.59, 0.41]],
        'K': [['aaa', 'aag'], [0.58, 0.42]],
        'V': [['gtt', 'gtc', 'gta', 'gtg'], [0.39, 0.21, 0.21, 0.19]],
        'D': [['gat', 'gac'], [0.65, 0.35]],
        'E': [['gaa', 'gag'], [0.71, 0.29]],
        'S': [['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'], [0.26, 0.16, 0.21, 0.10, 0.16, 0.11]],
        'C': [['tgt', 'tgc'], [0.63, 0.37]], 
        'W': [['tgg'], [1.00]], 
        'P': [['cct', 'ccc', 'cca', 'ccg'], [0.31, 0.15, 0.41, 0.12]], 
        'R': [['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg'], [0.15, 0.06, 0.07, 0.04, 0.48, 0.02]], 
        'T': [['act', 'acc', 'aca', 'acg'], [0.35, 0.22, 0.30, 0.13]],  
        'A': [['gct', 'gcc', 'gca', 'gcg'], [0.38, 0.22, 0.29, 0.11]],
        'G': [['ggt', 'ggc', 'gga', 'ggg'], [0.47, 0.19, 0.22, 0.12]],
        'end': [['taa', 'tag', 'tga'], [0.48, 0.24, 0.29]]}}

#bcl-2= MAQAGRTGYDNREIVMKYIHYKLSQRGYEWDVGDVDAAPLGAAPTPGIFSFQPESNPTPAVHRDMAARTSPLRPIVATTGPTLSPVPPVVHLTLRRAGDDFSRRYRRDFAEMSSQLHLTPFTARGRFATVVEELFRDGVNWGRIVAFFEFGGVMCVESVNREMSPLVDNIALWMTEYLNRHLHTWIQDNGGWDAFVELYGPSVRPLFDFSWLSLKTLLSLALVGACITLGTYLGHK

p=input('please enter your protein sequence: ')
p=''.join(p.splitlines()).strip()
print('which host do you want to optimise for:\n1)Homosapien\n2)E. coli\n3)Yeast')
s=input('=')
sc=True
if s=='1' or s=='homosapien' or s=='Homosapiens' or s=='homosapiens':
    s='Homosapien'
elif s=='2' or s=='e.coli' or s=='E.coli':
    s='E. coli'
elif s=='3' or s=='yeast':
    s='Yeast'
elif (s in allspecies.keys())==False:
    sc=False
    print('invalid input!')    

if sc==True:
    sdict=allspecies.get(s)
    dna=''
    for aa in p:
        codons=sdict.get(aa)
        codon=codons[0][codons[1].index(max(codons[1]))]
        dna+=codon
    codons=sdict.get('end')
    codon=codons[0][codons[1].index(max(codons[1]))]
    dna+=codon
    mrna=dna.replace('t','u')
    print('----------------------------------\nOptimisation complete. Results:\n\nOptimised mRNA =\n', mrna ,'\n\nOptimised Dna for', s , '=\n', dna)
