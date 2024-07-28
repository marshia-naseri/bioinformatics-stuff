l=[['ala', 'A'],['gct', 'gcc', 'gca', 'gcg'],
['arg', 'R'], ['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg'],
['asn', 'N'], ['aat', 'aac'],
['asp', 'D'], ['gat', 'gac'],
['cys', 'C'], ['tgt', 'tgc'],
['gln', 'Q'], ['caa', 'cag'],
['glu', 'E'], ['gaa', 'gag'],
['gly', 'G'], ['ggt', 'ggc', 'gga', 'ggg'],
['his', 'H'], ['cat', 'cac'],
['ile', 'I'], ['att', 'atc', 'aua'],
['leu', 'L'], ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'],
['lys', 'K'], ['aaa', 'aag'],
['met', 'M'], ['atg'],
['phe', 'F'], ['ttt', 'ttc'],
['pro', 'P'], ['cct', 'ccc', 'cca', 'ccg'],
['ser', 'S'], ['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'],
['thr', 'T'], ['act', 'acc', 'aca', 'acg'],
['trp', 'W'], ['tgg'],
['tyr', 'Y'], ['tat', 'tac'],
['val', 'V'], ['gtt', 'gtc', 'gta', 'gtg']]
end=['tag', 'taa', 'tga']

#dna sample: TRP53A=atggaggagccgcagtcagatcctagcgtcgagccccctctgagtcaggaaacattttcagacctatggaaactacttcctgaaaacaacgttctgtcccccttgccgtcccaagcaatggatgatttgatgctgtccccggacgatattgaacaatggttcactgaagacccaggtccagatgaagctcccagaatgccagaggctgctccccccgtggcccctgcaccagcagctcctacaccggcggcccctgcaccagccccctcctggcccctgtcatcttctgtcccttcccagaaaacctaccagggcagctacggtttccgtctgggcttcttgcattctgggacagccaagtctgtgacttgcacgtactcccctgccctcaacaagatgttttgccaactggccaagacctgccctgtgcagctgtgggttgattccacacccccgcccggcacccgcgtccgcgccatggccatctacaagcagtcacagcacatgacggaggttgtgaggcgctgcccccaccatgagcgctgctcagatagcgatggtctggcccctcctcagcatcttatccgagtggaaggaaatttgcgtgtggagtatttggatgacagaaacacttttcgacatagtgtggtggtgccctatgagccgcctgaggttggctctgactgtaccaccatccactacaactacatgtgtaacagttcctgcatgggcggcatgaaccggaggcccatcctcaccatcatcacactggaagactccagtggtaatctactgggacggaacagctttgaggtgcgtgtttgtgcctgtcctgggagagaccggcgcacagaggaagagaatctccgcaagaaaggggagcctcaccacgagctgcccccagggagcactaagcgagcactgcccaacaacaccagctcctctccccagccaaagaagaaaccactggatggagaatatttcacccttcagatccgtgggcgtgagcgcttcgagatgttccgagagctgaatgaggccttggaactcaaggatgcccaggctgggaaggagccaggggggagcagggctcactccagccacctgaagtccaaaaagggtcagtctacctcccgccataaaaaactcatgttcaagacagaagggcctgactcagactga
print('---------------------------------------')
dna=input('enter original dna sequence : ')
mdna=input('enter mutated dna sequence : ')
p=''
stop=0
for i in range(0,len(dna), 3):
    c3=dna[i:i+3]
    if (c3 in end)==True:
        stop=i//3
        print(c3)
        break
    for z in range(1,len(l),2):
        if (c3 in l[z])==True:
            p=p+l[z-1][1]
            break


mp=''
for i in range(0, len(mdna), 3):
    c3=mdna[i:i+3]
    if (c3 in end)==True:
        mstop=i//3
        print(c3)
        break
    for z in range(1,len(l),2):
        if (c3 in l[z])==True:
            mp=mp+l[z-1][1]
            break

print(stop, mstop)
print('--------------------------------------- \n results: \n')
print('original protein= ', p, '\n')
print('mutated  protein= ', mp, '\n')
count=0
if len(p)==len(mp):
    for i in range(0,len(p)):
        if p[i]!=mp[i]:
            print('misssense mutation at position: ', i , mp[i], 'replaces', p[i])
            count=1
    if count==0:
        print('this is a silent mutation')
if mstop<stop:
    print('nonsense mutation: translation stops at position:', mstop)

print('\n thanks for using the program')
        
    
    
