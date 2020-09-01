#for partial pivoting
def partial_pivot(R):
    n=len(R)
    for f in range(n-1):
        if R[f][f]==0:
            for k in range(f+1,n):
                if abs(R[k][f])>abs(R[f][f]):
                    R[f],R[k]=R[k],R[f]
                else: continue
        else: continue
#for gauss jordan method
def gau_jor(x):
    partial_pivot(x)
    for i in range(n):
        piv_e=x[i][i]
        if piv_e!=0:
            for k in range(i,n+1):
                x[i][k]=float(x[i][k])/float(piv_e)
            for r in range(n):
                if r==i or x[r][i]==0: continue
                else:
                    subtr=x[r][i]
                    for k in range(i,n+1):
                        x[r][k]=x[r][k]-subtr*x[i][k]
#for multiplication
def multiply(a,b,ab):
    m=len(a)
    for i in range(m):
        for j in range(m):
            for k in range(m):
                ab[i][j]+=a[i][k]*b[k][j]
print("Question 1 :")
f=open('Ass3Q1.txt', 'r')
A=[[int(num) for num in line.split(' ')] for line in f]
n=3
partial_pivot(A)
gau_jor(A);
for i in range(n):
    print(f'x{i+1}={A[i][n]}')
print("Question 2:")
f=open('Ass3Q2.txt', 'r')
A=[[int(num) for num in line.split(' ')] for line in f]
partial_pivot(A)
gau_jor(A);
for i in range(n):
    print(f'x{i+1}={A[i][n]}')
Aug=[[0 for j in range(2*n)] for i in range(n)]
for i in range(n):
    for j in range(2*n):
        if j<3: Aug[i][j]=A[i][j]
        else:
            m=j-3
            if m==i: Aug[i][j]=1
partial_pivot(Aug)
gau_jor(Aug)
Ainv=[[0 for j in range(n)]for i in range(n)]
I=[[0 for j in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
     if i==j: I[i][j]=1
AA_1=[[0 for j in range(n)]for i in range(n)]
multiply(A,Ainv,AA_1)
if AA_1==I:
    print("the property is checked")







