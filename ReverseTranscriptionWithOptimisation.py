n=''
while n!='q':
    p=input('--------------------------------------------------- \n please enter your protein sequence= ')
    l=int(input('\n which host do you want to recieve an optimised gene for: \n 1)Homo Sapien \n 2)E. Coli \n 3)Yeast \n = '))
    p=list(p)
    sp=['', 'homo sapien', 'E. coli', 'yeast']
    everything=['', [ #homosapien
                ['phe', 'F'], ['ttt', 'ttc'], [0.45, 0.55],
                ['leu', 'L'], ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'], [0.07, 0.13, 0.13, 0.20, 0.07, 0.41],
                ['tyr', 'Y'], ['tat', 'ttv'], [0.43, 0.57],
                ['his', 'H'], ['cat', 'cac'], [0.41, 0.59],
                ['glu', 'Q'], ['caa', 'cag'], [0.25, 0.75],
                ['ile', 'I'], ['att', 'atc', 'ata'], [0.36, 0.48, 0.16],
                ['met', 'M'], ['atg'], [1.00],
                ['asn', 'N'], ['aat', 'aac'], [0.46, 0.54],
                ['lys', 'K'], ['aaa', 'aag'], [0.42, 0.58],
                ['val', 'V'], ['gtt', 'gtc', 'gta', 'gtg'], [0.18, 0.24, 0.11, 0.47],
                ['asp', 'D'], ['gat', 'gac'], [0.46, 0.54],
                ['glu', 'E'], ['gaa', 'gag'], [0.42, 0.58],
                ['ser', 'S'], ['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'], [0.18, 0.22, 0.15, 0.06, 0.14, 0.24], 
                ['cys', 'C'], ['tgt', 'tgc'], [0.45, 0.56],
                ['trs', 'W'], ['tgg'], [1.00],
                ['pro', 'P'], ['cct', 'ccc', 'cca', 'ccg'], [0.28, 0.33, 0.27, 0.11],
                ['arg', 'R'], ['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg'], [0.08, 0.19, 0.11, 0.21, 0.20, 0.20],
                ['thr', 'T'], ['act', 'acc', 'aca', 'acg'], [0.24, 0.36, 0.28, 0.12],
                ['ala', 'A'], ['gct', 'gcc', 'gca', 'gcg'], [0.26, 0.40, 0.23, 0.11],
                ['gly', 'G'], ['ggt', 'ggc', 'gga', 'ggg'], [0.16, 0.34, 0.25, 0.25],
                ['end'], ['taa', 'tag', 'tga'], [0.28, 0.20, 0.52]
                ], [ #e.coli
                ['phe', 'F'], ['ttt', 'ttc'], [0.58, 0.42],
                ['leu', 'L'], ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'], [0.14, 0.13, 0.12, 0.10, 0.04, 0.47],
                ['tyr', 'Y'], ['tat', 'ttv'], [0.59, 0.41],
                ['his', 'H'], ['cat', 'cac'], [0.57, 0.43],
                ['glu', 'Q'], ['caa', 'cag'], [0.34, 0.66],
                ['ile', 'I'], ['att', 'atc', 'ata'], [0.49, 0.39, 0.11],
                ['met', 'M'], ['atg'], [1.00],
                ['asn', 'N'], ['aat', 'aac'], [0.49, 0.51],
                ['lys', 'K'], ['aaa', 'aag'], [0.74, 0.26],
                ['val', 'V'], ['gtt', 'gtc', 'gta', 'gtg'], [0.28, 0.20, 0.17, 0.35],
                ['asp', 'D'], ['gat', 'gac'], [0.63, 0.37],
                ['glu', 'E'], ['gaa', 'gag'], [0.68, 0.32],
                ['ser', 'S'], ['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'], [0.17, 0.15, 0.14, 0.14, 0.16, 0.25],
                ['cys', 'C'], ['tgt', 'tgc'], [0.46, 0.54],
                ['trs', 'W'], ['tgg'], [1.00],
                ['pro', 'P'], ['cct', 'ccc', 'cca', 'ccg'], [0.18, 0.13, 0.20, 0.49],
                ['arg', 'R'], ['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg'], [0.36, 0.35, 0.08, 0.11, 0.07, 0.04],
                ['thr', 'T'], ['act', 'acc', 'aca', 'acg'], [0.19, 0.40, 0.17, 0.25],
                ['ala', 'A'], ['gct', 'gcc', 'gca', 'gcg'], [0.18, 0.26, 0.23, 0.33],
                ['gly', 'G'], ['ggt', 'ggc', 'gga', 'ggg'], [0.35, 0.37, 0.13, 0.15],
                ['end'], ['taa', 'tag', 'tga'], [0.61, 0.09, 0.30]
                ], [ #yeast
                ['phe', 'F'], ['ttt', 'ttc'], [0.59, 0.41],
                ['leu', 'L'], ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'], [0.28, 0.29, 0.13, 0.06, 0.14, 0.11],
                ['tyr', 'Y'], ['tat', 'ttv'], [0.56, 0.44],
                ['his', 'H'], ['cat', 'cac'], [0.64, 0.36],
                ['glu', 'Q'], ['caa', 'cag'], [0.69, 0.31],
                ['ile', 'I'], ['att', 'atc', 'ata'], [0.46, 0.26, 0.27],
                ['met', 'M'], ['atg'], [1.00],
                ['asn', 'N'], ['aat', 'aac'], [0.59, 0.41],
                ['lys', 'K'], ['aaa', 'aag'], [0.58, 0.42],
                ['val', 'V'], ['gtt', 'gtc', 'gta', 'gtg'], [0.39, 0.21, 0.21, 0.19],
                ['asp', 'D'], ['gat', 'gac'], [0.65, 0.35],
                ['glu', 'E'], ['gaa', 'gag'], [0.71, 0.29],
                ['ser', 'S'], ['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'], [0.26, 0.16, 0.21, 0.10, 0.16, 0.11],
                ['cys', 'C'], ['tgt', 'tgc'], [0.63, 0.37],
                ['trs', 'W'], ['tgg'], [1.00],
                ['pro', 'P'], ['cct', 'ccc', 'cca', 'ccg'], [0.31, 0.15, 0.41, 0.12],
                ['arg', 'R'], ['cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg'], [0.15, 0.06, 0.07, 0.04, 0.48, 0.021],
                ['thr', 'T'], ['act', 'acc', 'aca', 'acg'], [0.35, 0.22, 0.30, 0.13],
                ['ala', 'A'], ['gct', 'gcc', 'gca', 'gcg'], [0.38, 0.22, 0.29, 0.11],
                ['gly', 'G'], ['ggt', 'ggc', 'gga', 'ggg'], [0.47, 0.19, 0.22, 0.12],
                ['end'], ['taa', 'tag', 'tga'], [0.48, 0.24, 0.29]
                ]]

    l2=everything[l]
    a=l2[0]
    b=l2[1]
    c=l2[2]

    dna=''
    for i in range(0,len(p)):
        d=p[i]
        for z in range(0, len(l2), 3):
            a=l2[z]
            b=l2[z+1]
            c=l2[z+2]
            if (d in a)==True:
                dna=dna+(b[c.index(max(c))])
                break

    print('--------------------------------------------------- \n the dna sequence optimised for', sp[l], 'is => ', dna)
    n=input('--------------------------------------------------- \n press enter to start over or "q" to stop the program=  ')
                
        
            











                       

    
