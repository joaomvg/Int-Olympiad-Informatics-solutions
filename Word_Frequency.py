#simple program to determine frequency of words in some input

phrase=input("Write something: ")
y=[]
x=[]
l=len(phrase)

i=0

for i in range(0,l):

    if phrase[i]!=' ':
        x.append(phrase[i])
    else:
        if len(x) != 0: y.append(x)
        x=[]

    if phrase[i]!=' ' and i==l-1:
        y.append(x)

L=len(y)

for i in range(0,L):
    y[i]=''.join(y[i]) #joins the characters in the list to make a single string


z=[]

while L!=0:

    k=0
    for i in range(0,L):
       if y[i]==y[0]:
           k+=1

    z.append([y[0],k])

    for i in range(0,k):
        y.remove(y[0])

    L=len(y)

print(z)
