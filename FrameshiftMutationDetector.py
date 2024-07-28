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

def transcript(dna):
    mrna=dna.replace('t','u')
    return mrna
def align(seq1, seq2):
    print('start alignment')
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
    print('finish alignment')
    return [res1,res2]

def frameshift_detector(dna,mdna):
    print('start frameshift process')
    frameshift=False
    if (len(dna)-len(mdna))%3==0:
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
#dna sample: TRP53A=atggaggagccgcagtcagatcctagcgtcgagccccctctgagtcaggaaacattttcagacctatggaaactacttcctgaaaacaacgttctgtcccccttgccgtcccaagcaatggatgatttgatgctgtccccggacgatattgaacaatggttcactgaagacccaggtccagatgaagctcccagaatgccagaggctgctccccccgtggcccctgcaccagcagctcctacaccggcggcccctgcaccagccccctcctggcccctgtcatcttctgtcccttcccagaaaacctaccagggcagctacggtttccgtctgggcttcttgcattctgggacagccaagtctgtgacttgcacgtactcccctgccctcaacaagatgttttgccaactggccaagacctgccctgtgcagctgtgggttgattccacacccccgcccggcacccgcgtccgcgccatggccatctacaagcagtcacagcacatgacggaggttgtgaggcgctgcccccaccatgagcgctgctcagatagcgatggtctggcccctcctcagcatcttatccgagtggaaggaaatttgcgtgtggagtatttggatgacagaaacacttttcgacatagtgtggtggtgccctatgagccgcctgaggttggctctgactgtaccaccatccactacaactacatgtgtaacagttcctgcatgggcggcatgaaccggaggcccatcctcaccatcatcacactggaagactccagtggtaatctactgggacggaacagctttgaggtgcgtgtttgtgcctgtcctgggagagaccggcgcacagaggaagagaatctccgcaagaaaggggagcctcaccacgagctgcccccagggagcactaagcgagcactgcccaacaacaccagctcctctccccagccaaagaagaaaccactggatggagaatatttcacccttcagatccgtgggcgtgagcgcttcgagatgttccgagagctgaatgaggccttggaactcaaggatgcccaggctgggaaggagccaggggggagcagggctcactccagccacctgaagtccaaaaagggtcagtctacctcccgccataaaaaactcatgttcaagacagaagggcctgactcagactga
print('---------------------------------------')
dna=input('enter original dna sequence : ')
dna=(''.join(dna.splitlines())).strip()
mdna=input('enter mutated dna sequence : ')
mdna=(''.join(mdna.splitlines())).strip()
p=translate(dna)
mp=translate(mdna)
p=p.ljust(len(mp),'x')
mp=mp.ljust(len(p),'x')
aach=[]
for i in range(len(p)):
    if p[i]!=mp[i] and p!='x' and mp!='x':
        aach.append(i)
results=frameshift_detector(dna,mdna)
print(f"--------------------------------\nresults:\noriginal protein: {p}\nmutated protein: {mp}\nframeshift detection= {results}\naminoacids change at positions: {aach}")

