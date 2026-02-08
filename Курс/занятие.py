'''a = int(input())
k=0
while a != 0:
    n=a
    a=int(input())
    if a>n:
        k+=1
print(k)'''
#########################################
'''N = int(input())
a = int(input())
k = int(input())
p=0
while N>0:
    if N%10==a:
        p+=1
    N=N//10
if p>k:
    print("YES")
else:
    print("NO")'''
#########################################
'''p=int(input())
v=int(input())
flag=1
k=1
while v != 0:
    if p==v and flag==1:
        k+=1
    else:
        flag=0
    p=v
    v=int(input())
print(k)'''
#########################################
'''a=int(input())
flag=0
d=2
while d*d<=a:
    if a%d==0:
        print("NO")
        flag=1
    d+=1
if flag==0:
    print("YES")'''
#########################################
'''n=int(input())
p1=1
p2=1
for i in range (3,n+1):
    p1,p2=p2,p1+p2
print(p2)'''
#########################################
'''n=int(input())
p1=1
p2=1
print(p1)
print(p2)
for i in range(3,n+1):
    p1,p2=p2,p1+p2
    print(p2)'''
#########################################
'''n=int(input())
Sum=0
for i in range (1,n+1):
    Sum+=i**(n-i+1)
print(Sum)'''
#########################################
'''N=int(input("Введите число N"))
array=[]
print("введите элементы массива")
for i in range(N):
  element=int(input())
  array.append(element)
doubled_array=[x*2 for x in array]
print("Полученный массив:", doubled_array)'''
#########################################
'''a = int(input())
a = (a//60)%60
print (a)'''
####################
'''n=int(input())
p=3.14
print(p*n)'''
####################
'''N=int(input())
element=input()
mas=[]
print()
for i in range(N):
  mas.append(element)
mas=[x*2 for x in mas]
print(mas, end=' ')'''
###################################
'''def F(n):
  if n > 0:
    F(n - 3)
    print(n, end="")
    F(n // 3)
print (F(9))'''
###################################