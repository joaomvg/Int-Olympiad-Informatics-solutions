# Write a program that calculates the highest sum of numbers passed on a route that starts at the top and ends somewhere on the base.
# Each step can go either diagonally down to the left or diagonally down to the right.
# The number of rows in the triangle is >1 but <=100.
# The numbers in the triangle, all integers, are between 0 and 99.

def trim(x): #for the input. to extract the relevant numbers
    z=""
    w=[]
    d=len(x)
    i=0
    while i<d:
        if x[i]!=" ":
            z+=x[i]
        elif z!="":
            z=int(z)
            w.append(z)
            z=""
        if i==d-1 and z!="":
            z=int(z)
            w.append(z)
        i+=1

    return w

def max(a):
    l=len(a)
    b=a[0]

    for i in range(0,l):
        if a[i]>=b:
            b=a[i]

    return b

num_r=input("Number of rows: ")
num_r=int(num_r)


tri=[]
for i in range(0,num_r):
    line=input()
    tri.append(trim(line))

sum=[]
z=[tri[0][0],tri[0][0]]


for i in range(1,num_r):

    D=len(tri[i])
    d=2+2*(D-2)

    w=[0]*d #2nd duplicate
    w[0]=tri[i][0]
    w[d-1]=tri[i][D-1]

    for k in range(1,D-1): #duplicates
        for u in range(0,2):
            w[2*k-u]=tri[i][k]

    for j in range(0,d):
      w[j]+=z[j]

    y = [0] * D

    y[0]=w[0]
    y[D-1]=w[d-1]

    for k in range(1,D-1): #duplicates
        if w[2*k-1]<=w[2*k]:
            y[k]=w[2*k]
        else:
            y[k]=w[2*k-1]

    z=[0]*2*D

    for i in range(0,D):
        z[2*i]=y[i]
        z[2*i+1]=y[i]


print(max(w))




