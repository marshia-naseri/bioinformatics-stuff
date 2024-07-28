l=[['ala', 'A'],['gcu', 'gcc', 'gca', 'gcg'],
['arg', 'R'], ['cgu', 'cgc', 'cga', 'cgg', 'aga', 'agg'],
['asn', 'N'], ['aau', 'aac'],
['asp', 'D'], ['gau', 'gac'],
['cys', 'C'], ['ugu', 'ugc'],
['gln', 'Q'], ['caa', 'cag'],
['glu', 'E'], ['gaa', 'gag'],
['gly', 'G'], ['ggu', 'ggc', 'gga', 'ggg'],
['his', 'H'], ['cau', 'cac'],
['ile', 'I'], ['auu', 'auc', 'aua'],
['leu', 'L'], ['uua', 'uug', 'cuu', 'cuc', 'cua', 'cug'],
['lys', 'K'], ['aaa', 'aag'],
['met', 'M'], ['aug'],
['phe', 'F'], ['uuu', 'uuc'],
['pro', 'P'], ['ccu', 'ccc', 'cca', 'ccg'],
['ser', 'S'], ['ucu', 'ucc', 'uca', 'ucg', 'agu', 'agc'],
['thr', 'T'], ['acu', 'acc', 'aca', 'acg'],
['trp', 'W'], ['ugg'],
['tyr', 'Y'], ['uau', 'uac'],
['val', 'V'], ['guu', 'guc', 'gua', 'gug']]
stop=['uaa','uag','uga']
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
    
print('______________________' , '\n')
m=input('please enter your mrna code: ')
m=(''.join(m.splitlines())).strip()
if ('t' in m)==True:
    print('this is a dna sequence but I am a kind program.')
    m=transcript(m)
p=translate(m)
print('--------------------------------------' ,'\n' , 'your protein is \n => ' , p , '\n' , '--------------------------------------')
print('thanks for using the program')
    
