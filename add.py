a=[[1,2,15],
    [1,3,20],
    [2,1,14],
    [2,2,20]]

b=[[1,2,10],
    [1,3,10],
    [3,1,14],
    [3,2,10]]

def sparse(a,b):
    ra=len(a)
    ca=len(a[0])
    rb=len(b)
    cb=len(b[0])
    add=[]
    cnt=0
    #print(ra, ca)
    for i in range(ra):
        for j in range(ca-1):
            print(a[i][j], end=' ')
            if(a[i][j]=b[i][j]):
                if(a[i][j+1]==b[i][j+1]):
                    c=[]
                    add.append(c)
                    add[cnt].append()
        print()
    l=ra+rb
    

sparse(a,b)
