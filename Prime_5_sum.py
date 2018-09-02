#this program writes all the primes with 5 digits and whose sum is specified

#x=input("Write Int (5 digits and sum=): ")
#x=int(x)

def Prime(x):
    n=int(pow(x,0.5)) #max divisor to run for
    k=0
    for i in range(2,n+2):
        m=x % i
        if m==0:
            k+=1
    if k==0:
        return 1
    else:
        return 0

def sum(a,m):
    s=0
    for i in range(0,m):
        s+=a[i]
    return s

def array_num(x):
    y=''.join(str(e) for e in x) #creates string out of the elements of the array x
    y=int(y) #converts string to integer

    return y

def test(a,m):
    k=0
    for i in range(0,m):
        if a[i]==0:
            k+=1
    if k==0:
        return 1
    else:
        return 0

m=5
s=int(input("Sum: "))
n=int(input("Integer: "))


list1=[]

#determine smax
if s<=9:
    smax=s*pow(10,4)
else:
    smax=0
    a=int(s/9)
    for i in range(0,a):
        smax+=9*pow(10,4-i)
    smax+=(s-a*9)*pow(10,4-a)

for i in range(pow(10,m-1)+1,smax,2):
    a=[int(i) for i in str(i)]

    if a[m-1]%5!=0:
        x=sum(a,m)
        l=Prime(i)
        if x==s and a[0]==n and l==1:
            list1.append(a)

dim_n=len(list1)
print(dim_n)

# for i in range(0,dim_n):
#     print(list1[i])

#auxiliary sequence
gen=[]
for i in range(0,10):
    gen.append(i)

#the code to build matrix mxm

for i,j,l in [(i,j,l) for i in range(0,dim_n) for j in range(0,dim_n) for l in range(0,dim_n)]:
    if test(list1[i],m)==1 and test(list1[j],m)==1: #compute diagonal
        rem_S=s-list1[i][4]-list1[j][4]-list1[l][2] #remaining sum
        if rem_S>=0 and rem_S<=18:
            #write sequence of interest for r<=9
            gn=(i for i in range(0,rem_S+1) if i in gen)
            for r in gn:
                n_aux=list1[j][4]*pow(10,4)+list1[l][2]*pow(10,2)+list1[i][4]+(rem_S-r)*pow(10,3)+r*pow(10,1)
                if (rem_S-r)<=9 and Prime(n_aux)==1:
                    rem_S2=s-list1[i][1]-list1[l][1]-(rem_S-r) #p1: second column
                    if rem_S2>=0 and rem_S2<=18:
                        gn2 = (i for i in range(0, rem_S2 + 1) if i in gen)
                        for r2 in gn2:
                            n_aux2 = list1[i][1] * pow(10, 4) + list1[l][1] * pow(10, 3) +(rem_S2-r2)*pow(10,2) +(rem_S-r)*pow(10,1)+ r2
                            if (rem_S2-r2)<=9 and Prime(n_aux2) == 1:
                                rem_S3 = s - list1[j][1] - list1[l][1] -r  # q1: second line
                                if rem_S3 >= 0 and rem_S3<=18:
                                    gn3 = (i for i in range(0, rem_S3 + 1) if i in gen)
                                    for r3 in gn3:
                                        n_aux3 = list1[j][1] * pow(10, 4) + list1[l][1] * pow(10, 3) + (rem_S3 - r3) * pow(10, 2) + r* pow(10, 1) + r3
                                        if (rem_S3-r3)<=9 and Prime(n_aux3) == 1:
                                            rem_S4 = s - list1[i][2] - (rem_S3-r3)-list1[l][2]  # p2: third column
                                            if rem_S4 >= 0 and rem_S4<=18:
                                                gn4 = (i for i in range(0, rem_S4 + 1) if i in gen)
                                                for r4 in gn4:
                                                    n_aux4 = list1[i][2] * pow(10, 4) + (rem_S3-r3)*pow(10,3)+list1[l][2] * pow(10, 2) + (rem_S4 - r4) * pow(10, 1) +r4
                                                    if (rem_S4-r4)<=9 and Prime(n_aux4) == 1:
                                                        rem_S5 = s - list1[j][2] - (rem_S2 - r2) - list1[l][2]  # q2: third line
                                                        if rem_S5 >= 0 and rem_S5<=18:
                                                            gn5 = (i for i in range(0, rem_S5 + 1) if i in gen)
                                                            for r5 in gn5:
                                                                n_aux5 = list1[j][2] * pow(10,4) + (rem_S2 - r2) * pow(10,3) + list1[l][2] * pow(10, 2) + (rem_S5 - r5) * pow(10,1) + r5
                                                                if (rem_S5-r5)<=9 and Prime(n_aux5) == 1:
                                                                    rem_S6 = s - list1[j][4] - r2-r4 - list1[l][4]
                                                                    if rem_S6>0 and rem_S6<=9:
                                                                        n_aux6 = list1[j][4]*pow(10,4) + r2*pow(10, 3) + r4*pow(10, 2) + (rem_S6) * pow(10, 1) + list1[l][4]
                                                                        if Prime(n_aux6) == 1:
                                                                            r6=s-list1[i][4]-r3-r5-list1[l][4]
                                                                            if r6>0:
                                                                                line1=list1[j][3]*pow(10,4)+(rem_S-r)*pow(10,3)+(rem_S4-r4)*pow(10,2)+list1[l][3]*pow(10,1)+r6
                                                                                colm1=list1[i][3]*pow(10,4)+r*pow(10,3)+(rem_S5-r5)*pow(10,2)+list1[l][3]*pow(10,1)+rem_S6
                                                                                colm2=list1[i][4]*pow(10,4)+r3*pow(10,3)+r5*pow(10,2)+r6*pow(10,1)+list1[l][4]
                                                                                z1=Prime(line1)
                                                                                z3=Prime(colm1)
                                                                                z4=Prime(colm2)
                                                                                y1=list1[j][3]+rem_S-r+rem_S4-r4+list1[l][3]+r6
                                                                                y3=list1[i][3]+r+rem_S5-r5+list1[l][3]+rem_S6

                                                                                if z1==1 and z3==1 and z4==1 and y1==s and y3==s:
                                                                                    print("Solution:")
                                                                                    print("________")
                                                                                    print(array_num(list1[i]))
                                                                                    print(n_aux3)
                                                                                    print(n_aux5)
                                                                                    print(line1)
                                                                                    print(n_aux6)
