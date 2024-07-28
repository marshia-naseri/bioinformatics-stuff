import math
def nernst(inC, outC, charge):
    constant=61.54/charge
    C=math.log((outC/inC),10)
    eq=constant * C
    return eq
c=int(input('enter the charge of the ion, with + or -: '))
a=float(input('enter the concentration of the inside fluid; '))
b=float(input('enter the concentration of the outside fluid: '))
print(nernst(a,b,c))