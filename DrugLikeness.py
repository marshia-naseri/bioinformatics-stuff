# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:59:34 2024

@author: arshia
"""

filters={'Lipinski': {'MW': 500,
                      'MLOGP': 4.15,
                      'hydrogen bond acceptors': 10,
                      'hydrogen bond donors': 5},
         'ghose': {'MW': (160,480),
                   'WLOGP': (-0.4,5.6),
                   'refractivity': 130,
                   'number of atom': (20,70)},
         'Veber': {'rotatable bonds': 10,
                   'TPSA': 140},
         'Egan': {'WLOGP': 5.88,
                  'TPSA': 131}}

print('please enter the following data.')
ml={}
for i in filters.keys():
    for x in filters[i].keys():
        if (x in ml.keys())==False:
            n=input(F"please enter the {x}: ")
            ml.setdefault(x,float(n))
res={}
for filt in filters:
    f=filters.get(filt)
    res[filt]={}
    for k in f:
        v=f[k]
        if type(v)==tuple:
            if ml[k]>=v[0] and ml[k]<=v[1]:
                res[filt][k]=True
            else:
                res[filt][k]=False
        else:
            if ml[k]<=v:
                res[filt][k]=True
            else:
                res[filt][k]=False

for i in res:
    mark=0
    r=[]
    for k,v in res[i].items():
        if v==False:
            mark=1
            r.append(k)
    if mark==1:
        print(f"\nThis compound is not druglike according to the {i} filter.\nReason(s): {r}\n")
        
    else:
        print(f"\nThis molecule is druglike according to the {i} filter.\n")
    