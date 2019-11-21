a=[[0,0,0,1],
    [0,1,0,1],
    [0,1,0,0],
    [0,0,2,0]]

b=[[0,20,0,0],
    [0,0,15,0],
    [0,24,0,0],
    [0,0,0,30]]

print('a:',a)
#print('b:',b)
#print(len(a[0]), len(a))

def check(a):
    count=0
    k=len(a)*len(a[0])
    for i in a:
        for j in i:
            if j==0:
                count+=1

    if(count>k/2):
        print('its a sparse matrix')

def sparse(a):
    r=len(a)
    c=len(a[0])
    cnt=0
    element=[]
    row=[]
    column=[]
    for i in a:
        cnt=0
        for j in i:
            if(j!=0):
                cnt+=1
                element.append(j)

        if cnt>0:
            row.append(cnt)
    for i in range(r):
        cnt=0
        for j in range(c):
            if(a[j][i]!=0):
                cnt+=1

        if cnt>0:
            column.append(cnt)

    sparse=[[len(row),len(column),len(element)]]
    cnt=1
    for i in range(r):
        for j in range(c):
            if(a[i][j]!=0):
                sp=[]
                sparse.append(sp)
                sparse[cnt].append(i+1)
                sparse[cnt].append(j+1)
                sparse[cnt].append(a[i][j])
                cnt+=1


    print('row=',row,'    column=',column)

    print('sp:= ',sparse)

#check(a)
sparse(a)
