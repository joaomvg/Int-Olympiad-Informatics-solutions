# There are nine clocks in a 3*3 array (figure 1). The goal is to return all the dials
# to 12 o'clock with as few moves as possible. There are nine different allowed ways to ' \
# 'turn the dials on the clocks. Each such way is called a move. Select for each move a' \
# ' number 1 to 9. That number will turn the dials 90' (degrees) clockwise on those
# clocks which are affected according to figure 2 below.

import numpy as np

def trim(x): #for the input. to extract the relevant numbers out od a string w/ spaces
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

def sum_matrix(a,b):
    d=len(a) #len a= len b

    x=np.array(a)
    y=np.array(b)
    w=x+y
    w=np.array(w).tolist()

    return w

def prod_matrix(x,a):
    #matrix x, constant a
    l=len(x)
    w=np.array(x)
    w=a*w
    w=np.array(w).tolist()

    return w

def mod_4(a): #a is matrix
    d=len(a)
    k=0
    for i in range(0,d):
        for j in range(0,d):
            if a[i][j]%4!=0 or k==1:
                k=1
                break
    return k

#define moves

move=[0]*9

move[0]=[[1,1,0],[1,1,0],[0,0,0]]
move[1]=[[1,1,1],[0,0,0],[0,0,0]]
move[2]=[[0,1,1],[0,1,1],[0,0,0]]
move[3]=[[1,0,0],[1,0,0],[1,0,0]]
move[4]=[[0,1,0],[1,1,1],[0,1,0]]
move[5]=[[0,0,1],[0,0,1],[0,0,1]]
move[6]=[[0,0,0],[1,1,0],[1,1,0]]
move[7]=[[0,0,0],[0,0,0],[1,1,1]]
move[8]=[[0,0,0],[0,1,1],[0,1,1]]


clock=[] #should have dim 3x3

print("Clock\n")
for i in range(0,3):
    line=input()
    clock.append(trim(line))

a=[0]*9
p=30

for i1 in range(0,4):
    a[0]=i1
    s1=prod_matrix(move[0],i1)
    for i2 in range(0, 4):
        a[1] = i2
        s2 = sum_matrix(prod_matrix(move[1], i2),s1)
        for i3 in range(0, 4):
            a[2] = i3
            s3 = sum_matrix(prod_matrix(move[2], i3), s2)
            for i4 in range(0, 4):
                a[3] = i4
                s4 = sum_matrix(prod_matrix(move[3], i4), s3)
                for i5 in range(0, 4):
                    a[4] = i5
                    s5 = sum_matrix(prod_matrix(move[4], i5), s4)
                    for i6 in range(0, 4):
                        a[5] = i6
                        s6 = sum_matrix(prod_matrix(move[5], i6), s5)
                        for i7 in range(0, 4):
                            a[6] = i7
                            s7 = sum_matrix(prod_matrix(move[6], i7), s6)
                            for i8 in range(0, 4):
                                a[7] = i8
                                s8 = sum_matrix(prod_matrix(move[7], i8), s7)
                                for i9 in range(0, 4):
                                    a[8] = i9
                                    s9 = sum_matrix(prod_matrix(move[8], i9), s8)

                                    m=sum_matrix(clock,s9)
                                    if mod_4(m)==0:

                                        k=0
                                        for v in range(0,9):
                                            k+=a[v]
                                        if k<=p:
                                            p=k
                                            solution=a[:]

print("Solution:\n")
print(solution)
count=0
for i in range(0,9):
    count+=solution[i]

print("Number of moves="+str(count))





