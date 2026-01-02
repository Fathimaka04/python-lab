# numbers count

n=[int(i) for i in input("enter the numberes").split()]
visited=[]
for i in n:
    if i not in visited:
        count=0
        for j in n:
            if i==j:
                count=count+1
        print(i,"->",count)
        visited.append(i)


# string count
n=input("enter a string").split()
visited=[]
for i in n:
    if i not  in visited:
        count=0
        for j in n:
            if i==j:
                count+=1
        visited.append(i)
        print(i,"->",count)

#patterns
n=int(input("enter how many rows you want"))
for i in range(1,n+1):
    
    for j in range (1,i+1):
        
        print(i*j,end=" ")
    print()

    #maximum length from  a word
    n=[i for i in input("enter a words").split()]
s=[]

for i in n:
    s.append(len(i))
print(s)
print(max(s))
 
 #pyramid
n=int(input("enter the number"))
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
   

#Write a program using def to find perfect square numbers in a given range where:

#The number is 3 digits

#Sum of digits is even

import math
def sumnum(num):
    sum=0
    while num>0:
        
        digit=num%10
        sum=sum+digit
        num=num//10
    return sum

def sumeven(num):
    t=sumnum(num)
    if t%2!=0:
        return False
    return True

def square(start,end):
    sq=[]
    for i in range(start,end+1):
        if i>=100 and i<=999 and sumeven(i):
            root=int(math.sqrt(i))
            if root*root==i:
                sq.append(i)
    return sq
s=int(input("enter a number"))
e=int(input("enter a numbber"))
f=square(s,e)
print(f)



#Write a program using def to find perfect cube numbers in a given range where:

#The number is 4 digits

#first digit is even and last digit is odd

import math
def evenfirst(num):
    first=num//1000
    if first%2!=0:
        return False
    return True
def oddlast(num):
    last=num%10
    if last%2==0:
        return False
    return True

def perfectcube(start,end):
    cubes=[]
    for i in range(start,end+1):
        if i>=1000 and i<9999 and evenfirst(i) and oddlast(i):
            root=int(math.cbrt(i))
            if root*root*root==i:
                cubes.append(i)
    return cubes 

    
   


s=int(input("enter a number"))
e=int(input("enter a numbber"))
f=perfectcube(s,e)
print(f)


#counting word or letters
n=input("enter the string").split()
res={}

for i in n:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
for w,c in res.items():
    print(f"{w}:{c}")


#pyramid down

n=int(input("enter  the number of rows"))
for i in range (n):
    for j in range(n-i):
        print("*",end=" ")
    print()

#pyramid triangle
n=int(input("enter  the number of rows"))
for i in range (1,n+1):
    for j in range(n-i):
        print("",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()