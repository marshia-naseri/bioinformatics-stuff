import random
def translate(mrna):
    protein=''
    for i in range(0,len(mrna),3):
        codon=mrna[i:i+3]
        if (codon in stop)==True:
            break
        for x in range(1,len(l),2):
            if (codon in l[x])==True:
                protein+=l[x-1][1]
                break
    return protein
def align(seq1, seq2):
    score_matrix=[]
    for i in range(len(seq1)+1):
        a=[]
        for j in range(0, len(seq2)+1):
            a.append(0)
        score_matrix.append(a)
    j=-3
    for i in range(1, len(score_matrix[0])):
        score_matrix[0][i]=j
        j=j-3
    j=-3
    for i in range(1, len(score_matrix)):
        score_matrix[i][0]=j
        j=j-3
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i]==seq2[j]:
                a1=score_matrix[i][j]+1
            else:
                a1=score_matrix[i][j]-1
            a2=score_matrix[i+1][j]-3
            a3=score_matrix[i][j+1]-3
            score_matrix[i+1][j+1]=max(a1,a2,a3)
    i=len(score_matrix)-2
    j=len(score_matrix[0])-2
    res1=''
    res2=''
    while i!=-1 and j!=-1:
        a=score_matrix[i+1][j+1]
        a1=score_matrix[i][j]
        a2=score_matrix[i+1][j]
        a3=score_matrix[i][j+1]
        if seq1[i]==seq2[j]:
            c=a-1
        else:
            c=a+1
        if c==a1:
            res1=seq1[i] + res1
            res2=seq2[j] + res2
            i=i-1
            j=j-1
        if a==a2-3:
            res1='-' + res1
            res2=seq2[j] + res2
            j=j-1
        if a==a3-3:
            res1=seq1[i] + res1
            res2='-' + res2
            i=i-1
    return [res1,res2]

def frameshift_detector(dna,mdna):
    frameshift=False
    if (len(dna)-len(mdna))%3==0 and (len(dna)-len(mdna))!=0:
        frameshift=True
    p=translate(dna)
    mp=translate(mdna)
    both=align(dna,mdna)
    d=both[0]
    md=both[1]
    p=p.ljust(len(mp))
    mp=mp.ljust(len(p))
    while ('-' in d)==True:
        mark=d.index('-')//3
        count=0
        for x in range(0,10):
            if not p[mark+x] or mp[mark+x]:
                break
            if p[mark+x]!=mp[mark+x]:
                count+=1
        if count>=5:
            frameshift==True
            break
        d=d.replace('-','',1)
    while ('-' in md)==True:
        mark=md.index('-')//3
        count=0
        for x in range(0,10):
            if p[mark+x]!=mp[mark+x]:
                count+=1
        if count>=5:
            frameshift=True
            break
        md=md.replace('-','',1)
    return frameshift

#dna sample= TRP53: atggaggagccgcagtcagatcctagcgtcgagccccctctgagtcaggaaacattttcagacctatggaaactacttcctgaaaacaacgttctgtcccccttgccgtcccaagcaatggatgatttgatgctgtccccggacgatattgaacaatggttcactgaagacccaggtccagatgaagctcccagaatgccagaggctgctccccccgtggcccctgcaccagcagctcctacaccggcggcccctgcaccagccccctcctggcccctgtcatcttctgtcccttcccagaaaacctaccagggcagctacggtttccgtctgggcttcttgcattctgggacagccaagtctgtgacttgcacgtactcccctgccctcaacaagatgttttgccaactggccaagacctgccctgtgcagctgtgggttgattccacacccccgcccggcacccgcgtccgcgccatggccatctacaagcagtcacagcacatgacggaggttgtgaggcgctgcccccaccatgagcgctgctcagatagcgatggtctggcccctcctcagcatcttatccgagtggaaggaaatttgcgtgtggagtatttggatgacagaaacacttttcgacatagtgtggtggtgccctatgagccgcctgaggttggctctgactgtaccaccatccactacaactacatgtgtaacagttcctgcatgggcggcatgaaccggaggcccatcctcaccatcatcacactggaagactccagtggtaatctactgggacggaacagctttgaggtgcgtgtttgtgcctgtcctgggagagaccggcgcacagaggaagagaatctccgcaagaaaggggagcctcaccacgagctgcccccagggagcactaagcgagcactgcccaacaacaccagctcctctccccagccaaagaagaaaccactggatggagaatatttcacccttcagatccgtgggcgtgagcgcttcgagatgttccgagagctgaatgaggccttggaactcaaggatgcccaggctgggaaggagccaggggggagcagggctcactccagccacctgaagtccaaaaagggtcagtctacctcccgccataaaaaactcatgttcaagacagaagggcctgactcagactga
dna=input('--------------------------------------------------- \n please enter the dna you wish to work on= ')

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
stop=['tag', 'taa', 'tga']
p=translate(dna)
print('---------------------------------------------------')
count=int(input('how many mutations do you want to apply:'))
print('please enter which mutation you want to apply: ',
      '\n 0: let the computer decide',
      '\n 1: substitution',
      '\n 2: deletion',
      '\n 3: insertion',
      '\n 4: inversion (5 nucleotides)',
      '\n 5: translocation (5 nucleotides)')
r=int(input('= '))
if r==0:
    r=random.randint(1,5)
n=['a', 't', 'c', 'g']
ncopy=n.copy()
mdna=list(dna)
while count>0:
    count=count-1
    if r==1:  #substitution
        loc=random.randint(3,len(mdna)-4)
        z=mdna[loc]
        n.remove(z)
        replace=n[random.randint(0,2)]
        mdna.pop(loc)
        mdna.insert(loc, replace)
        n=ncopy.copy()
        print(f"\n a substitution mutation was done: {z} from {loc+1} has been replaced by {replace}")
                        
    if r==2:  #deletion
        loc=random.randint(3,len(mdna)-4)
        z=mdna[loc]
        mdna.pop(loc)
        print(f"\n a deletion mutation was done: {z} from {loc+1} has been removed")
        
    if r==3:  #insertion
        insertion=''
        loc=random.randint(3,len(mdna)-4)
        z=mdna[loc]
        ins=n[random.randint(0,3)]
        insertion=insertion+ins
        mdna.insert(loc, ins)
        print(f"\n an insertion mutation was done: {insertion} has been inserted in {loc+1}")
        
    if r==4:  #inversion
        st=random.randint(3,len(mdna)-9)
        en=st + 5
        inv=mdna[st:en+1:]
        for i in range(st,en+1):
            mdna.pop(st)
        for i in range(0,len(inv)):
            mdna.insert(st, inv[i])
        print(f"\n an inversion mutation was done: {inv} from {st+1} to {en+1} has been inverted")

        
    if r==5:  #tranlocation
        st=random.randint(3,len(mdna)-9)
        en=st+5
        tran=mdna[st:en+1:]
        for i in range(st,en+1):
            mdna.pop(st)
        ins=random.randint(0,len(mdna)-1)
        for i in range(len(tran)-1, -1, -1):
            mdna.insert(ins, tran[i])
        print(f"\n a translocation mutation was done: {tran} from {st+1} to {en+1} has been translocated to {ins+1}")
mdna=''.join(mdna)
mp=translate(mdna)        
print(f"--------------------------------------------------- \nresults:\noriginal protein: {p} \n\nmutated protein: {mp}\n")
ch=[]
frameshift=frameshift_detector(dna,mdna)
if len(dna)>len(mdna):
        for i in range(0,len(mp)):
            if p[i]!=mp[i]:
                ch.append(i)

if len(mdna)>len(dna):
        for i in range(0,len(mp)):
            if p[i]!=mp[i]:
                ch.append(i)
print(f"frameshift is {frameshift}")

if len(p)>len(mp):
    print('this is a nonsense mutation : ' ,
          'translation stops at position:', len(mp))
    print('aminoacids lost: ', p[len(mp): len(p)])
p=p.ljust(len(mp),' ')
mp=mp.ljust(len(p),' ')
count=0
for i in range(len(p)):
    if p[i]!=mp[i] and p[i]!=' ' and mp[i]!=' ':
        print(f"a misssense mutation occurs at the {i+1} position : {p[i]} has been replaced with {mp[i]}")
        count=1
if count==0 and len(p)==len(mp):
    print('this is a silent mutation')

print('thanks for using the program')
