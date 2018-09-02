#Castle problem

#The file starts with the number of modules in the north-south direction and the number of modules in the east-west direction.
# In the following lines each module is described by a number (0<=p<=15). This number is the sum of: 1 (= wall to the west),
# 2 (= wall to the north), 4 (= wall to the east), 8 (= wall to the south). Inner walls are defined twice; a wall to the south in module 1,
# 1 is also indicated as a wall to the north in module 2,1.
# The castle always has at least two rooms.
import math

 #converts into binary code
n=input("Number= ")
n=int(n)
k=[]
x=""

pmax=math.log(n,2)
pmax=int(pmax)

for i in range(0,pmax+1):
    a=math.log(n,2)
    a=int(a)
    if a==pmax-i:
        x+="1"
        n-=pow(2, a)
        if n==0:
            break
    else:
        x+="0"

#reverse string
d=len(x)
y=""
for i in range(0,d):
    y+=x[d-1-i]

print(y)

