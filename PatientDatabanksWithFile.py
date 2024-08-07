# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:44:03 2024

@author: arshia
"""
import os
if os.path.isfile(r'G:\modules\bioinformatics\PatientsDatabank.txt')==False:
    patients={}
else:
    patients={}
    with open(r'G:\modules\bioinformatics\PatientsDatabank.txt','r') as file:
        for l in file.readlines():
            sets=l.split('()')
            sets.pop()
            pd={}
            mark=1
            for st in sets:
                kv=st.split(':')
                if mark==1:
                    name=kv[1]
                pd[kv[0]]=kv[1]
                mark+=1
            patients[name]=pd
            
        
g=''
while g!='6':
    print("\nWhat do you wish to do:\n1) View all patients\n2) Enter new patient data\n3) Update a patient's data\n4) Remove a patient data\n5) View patient data and treatment plan\n6) Save data and quit")
    g=input()
    
    if g=='1':
        print('\n--------------------------')
        n=0
        for name in patients.keys():
            n+=1
            print(n,':',name)
    
    elif g=='2':
        print('\n--------------------------')
        name=input('Enter patient name: ')
        while (name in patients.keys())==True:
            name+='*'
        age=input('Enter patient age: ')
        ttype=input('Enter type/name of neoplasia: ')
        tclass=input('Benign/malignant?: ')
        tstage=input('Enter tumor stage: ')
        patients[name]={'name':name, 'age':age, 'tumor type':ttype, 'tumor class':tclass, 'tumor stage':tstage}

        
    elif g=='3':
        print('\n--------------------------')
        oname=input('Enter patient name: ')
        if (oname in patients)==False:
            print('Patient not found!')
        else:
            patient=patients.get(oname)
            q=''
            while q!='6':
                print('1) name\n2) age\n3) tumor type\n4) tumor class\n5) tumor stage\n6) stop editing')
                n=input()
                if n=='1':
                    name=input('Enter updated name: ')
                    patient['name']=name
                elif n=='2':
                    age=input('Enter updated age: ')
                    patient['age']=age
                elif n=='3':
                    ttype=input('Enter updated tumor type: ')
                    patient['tumor type']=ttype
                elif n=='4':
                    tclass=input('Enter updated tumor class: ')
                    patient['tumor class']=tclass
                elif n=='5':
                    tstage=input('Enter updated tumor stage: ')
                    patient['tumor stage']=tstage
                elif n=='6':
                    q='6'
                else:
                    print('Invalid input!')
            patients.pop(oname)
            patients[name]=patient
            print('Patient data updated!')
        
    elif g=='4':
        name=input('Enter patient name: ')
        if (name in patients)==False:
            print('Patient not found!')
        else:
            patients.pop(name)
            print('Patient data removed!')
        
    elif g=='5':
        print('\n--------------------------')
        name=input('Enter patient name: ')
        print()
        if (name in patients)==False:
            print('Patient not found!')
        else:
            patient=patients.get(name)
            st=patient.get('tumor stage')
            ag=int(patient.get('age'))
            bm=patient.get('tumor class')
            if bm=='benign' or bm=='Benign':
                if ag<=50:
                    if st=='1' or st=='2':
                        patient['treatment plan']='1-1'
                    elif st=='3':
                        patient['treatment plan']='1-2'
                    elif st=='4':
                        patient['treatment plan']='1-3'
                    else:
                        print('Wrong input for tumor stage!')
                if ag>50:
                    if st=='1' or st=='2':
                        patient['treatment plan']='2-1'
                    elif st=='3' or st=='4':
                        patient['treatment plan']='2-2'
                    else:
                        print('Wrong input for tumor stage!')
            elif bm=='malignant' or bm=='Malignant': 
                if st=='1' or st=='2':
                    patient['treatment plan']='3-1'
                elif st=='3' or st=='4':   
                    patient['treatment plan']='3-2'
                else:
                    print('Wrong input for tumor stage!')
            else:
                print('Wrong input for tumor class!')
            patients[name]=patient
            patient=patients.get(name)
            for key,value in patient.items():
                print(key, ':', value)

    elif g=='6':
        with open(r'G:\modules\bioinformatics\PatientsDatabank.txt','w') as databank:
            for patient in patients.values():
                for i,j in patient.items():
                    gr=i+':'+j+'()'
                    databank.write(gr)
                databank.write('\n')
            print('Data saved!')

    else:
        print('Invalid input!)')
