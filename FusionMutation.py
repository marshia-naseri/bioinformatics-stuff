print("---------------------------------------------------")
dna1=input('please enter the first dna sequence: ')
print()
dna2=input('please enter the second dna sequence: ')
#dnasample" atggcccggagcgtgaccgtgatcttcctggtgctggtgagcctggccgtggtgctggccatccagaagaccccccagatccaggtgttvagccggcacccccccgagaacggcaagcccaacttcctgaactgcttvgtgagccagttccaccccccccagatcgagatcgagctgctgaagaacggcaagaagatccccaacatcgagatgagcgacctgagcttcagcaaggactggagcttcttvatcctggcccacaccgagttcacccccaccgagaccgacgtgttvgcctgccgggtgaagcacgtgaccctgaaggagcccaagaccgtgacctgggaccgggacatg
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

dna1_list=list(dna1)
dna2_list=list(dna2)
stop=len(dna1)//3
fp=''
for x in range(0, len(dna1)):
    fdna=[]
    dna1_list.pop()
    fdna.extend(dna1_list)
    fdna.extend(dna2_list)
    fdna3=[]
    for i in range(0,len(fdna),3):
        z=fdna[i:i+3]
        z2=''.join(z)
        fdna3.append(z2)
    for i in range(0,len(fdna3)):
        if (fdna3[i] in end) ==True:
            if i*3>(len(dna1_list)):
                stop=i
                fp=''
                for b in range(0, len(fdna3),):
                    c3=fdna3[b]
                    if (c3 in end)==True:
                        stop=b
                        break
                    for z in range(1, len(l) ,2):
                        if (c3 in l[z])==True:
                            fp=fp + (l[z-1][1])
                            break
                print('the second dna can be fused into the first one at position: ', len(dna1)-x)
                print()
                print('fused protein= ',fp)
                print('---------------------------------------------------')
                break
            break
 

        



