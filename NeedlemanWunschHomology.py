seq1=input('please enter first sequence= ')
seq1=(''.join(seq1.splitlines())).strip()
seq2=input('please enter second sequence= ')
seq2=(''.join(seq2.splitlines())).strip()
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
print()
print('aligned 1st sequence: ', res1)
print('aligned 2nd sequence: ', res2)

count=0
for i in range(len(res1)):
    if res1[i]!=res2[i]:
        count=count+1
    hom=((len(res1) - count)/len(res1))*100
print()
print('homology= ', hom)