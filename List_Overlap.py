#This program compares Lists and retrieves only the common entries without duplicates

a=[int(x) for x in input("Write List: ").split()]

n=len(a)
m=n

i=0
j=0

while i<n-1:
    j=i+1
    while j<n:
        if a[j]==a[i]:
            del a[j]
            n-=1
        else:
            j+=1

    i+=1

print(a)