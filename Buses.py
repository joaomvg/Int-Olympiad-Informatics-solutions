N=input()
N=int(N)

t_table=input()

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

t_table=trim(t_table)
t_aux=t_table[:]
d=len(t_table)
end=t_table[d-1]
buses=[]
line=[]

m=1
while True:
    init = t_aux[0]
    step=t_table[m]-init
    line.append(init)
    n=1

    while True:
        x=init+n*step
        if x not in t_table:
            break
        elif x<=end:
            line.append(x)
        n+=1
    if x>end:
        buses.append([init,step])
        for i in line:
            t_aux.remove(i)
    else:
        m+=1 #if not a bus then consider

