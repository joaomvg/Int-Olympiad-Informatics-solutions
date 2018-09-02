N=input()
N=int(N)

def check_box(box,N):
    d=len(box)

    a=0

    if d!=2*N:
        a=1

    for i in range(0,N-1):
        if box[i]!="A" and box[i]!="B":
            a=1
            break

    for i in range(N+1,2*N):
        if box[i]!="A" and box[i]!="B":
            a=1
            break

    if box[N-1]!="_" and box[N]!="_":
        a=1

    if a==0:
        return 1
    else:
        return 0



b=0

while b!=1:
    box = input()  # ababab--ababbab
    b = check_box(box, N)
    if b==1:
        print("Good box.")
    else:
        print("Box not ok, write again:")


l=2*N
box2=[0]*l

for i in range(0,N-1):
    if box[i]=="A":
        box2[i]=1
    elif box[i]=="B":
        box2[i]=0

box2[N-1]=2
box2[N]=2

for i in range(N+1,2*N):
    if box[i] == "A":
        box2[i]=1
    elif box[i] == "B":
        box2[i]=0

#print(box2)
a1=N-1
a2=N

def b2tb(box2):
    box=""

    for i in box2:
        if i==1:
            box+="A"
        if i==0:
            box+="B"
        if i==2:
            box+="_"

    return box