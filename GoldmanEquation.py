import math
def goldman():
    nain=15
    naout=150
    kin=100
    kout=5
    pk=40
    pna=1
    C=math.log10((pk*kout + pna*naout)/(pk*kin + pna*nain))
    goldman=61.54*C
    print(goldman)

goldman()