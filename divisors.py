#This program computes the number of divisors
x=input("Write integer number")

x=int(x) #number to find the divisors

n=int(x**0.5) #max divisor to run for
k=0

for i in range(1,n+1):
    m=x % i
    if m==0 and i!=n:
        k+=2
    elif m==0:
        k+=1

print(k)
