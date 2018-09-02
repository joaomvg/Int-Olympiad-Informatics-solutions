#Ask string and test whether the string reads the same forwards and backwards

s=input("Write something: ")
n=len(s)

for i in range(0,n):
    if s[i]!=s[n-1-i]:
        print("No it is not.")
        break
    elif i==n-1:
        print("It is!")






