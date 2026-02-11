#######################################
'''for n in range (1,150):
    n2=bin(n)[2:]
    if n2.count('1') %2==0:
        n2+='00'
    else:
        n2+='10'
    r=int(n2,2)
    if r>43:
        print(r)
        break'''
#######################################
'''for n in range (1,150):
    n2=bin(n)[2:]
    n2+=str(n2.count('1')%2)
    n2+=str(n2.count('1')%2)
    r=int(n2,2)
    if r>77:
        print(n)
        break'''
#######################################
'''for n in range (1,150):
    n2=bin(n)[2:]
    if n2.count('1')%2==0:
        n2+="00"
    else:
        n2+="11"
    r=int(n2,2)
    if r>114:
        print(r)
        break'''
#######################################
'''for n in range (1,150):
    n2=bin(n)[2:]
    if n2.count('1')%2==0:
        n2+='0'
    else:
        n2+='1'
    if n2.count('1')%2==0:
        n2+='0'
    else:
        n2+='1'
    r=int(n2,2)
    if r>97:
        print(r)'''
#######################################
'''for n in range (1,150):
    n2=bin(n)[2:]
    if n2.count('1')>n2.count('0'):
        n2+='1'
    else:
        n2+='0'
    r=int(n2,2)
    if r>80:
        print(r)'''
#######################################
'''for n in range (1,10000):
    n2=bin(n)[2:]
    n2=n2.replace('0','2')
    n2=n2.replace('1','0')
    n2=n2.replace('2','1')
    n2.strip('0')
    r=int(n2,2)
    if (n-r)==999:
        print(n)'''
#######################################
'''for n in range (1000000,1,-1):
    n2=bin(n)[2:]
    if n%5==0:
        n2+=bin(5)[2:]
    else:
        n2+='1'
    n2n=int(n2,2)
    if n2n%7==0:
        n2+=bin(7)[2:]
    else:
        n2+='1'
    r=int(n2,2)
    if r<1728404:
        print(n)
        break'''
#######################################
'''res=[]
for n in range (1,10000):
    n2=bin(n)[2:]
    if n2.count('1')%2==0:
        n2=n2+'10'
        if n2[1]=='1':
            n2=n2[2:]
        else:
            if n2[1]=='0':
                n2='1'+n2[2:]
    else:
        n2=n2+'11'
        if n2[1]=='1':
            n2=n2[2:]
        else:
            if n2[1]=='0':
                n2='1'+n2[2:]
    r=int(n2,2)
    if r>43:
        res.append(r)
print(min(res))'''
#######################################
'''def to_base4(n):
    res = ""
    while n > 0:
        res = str(n % 4) + res
        n //= 4
    return res
def from_base4(s):
    return int(s, 4)
for N in range(1, 1000):
    base4 = to_base4(N)
    if N % 4 == 0:
        R_base4 = base4[:-1]
    else:
        r = str(N % 4)
        R_base4 = r + base4 + r
    R = from_base4(R_base4)
    if R > 313:
        print(N)
        break'''
#######################################
'''res=[]
def tr(n):
    s=''
    while n>0:
        s=str(n%3)+s
        n//=3
    return s
for N in range (1,10000):
    n3=tr(N)
    if N%3==0:
        n3=n3+n3[-2:]
    else:
        a=int(n3)
        summ=0
        while a>0:
            summ=a%10
            a=a//10
        summ3=tr(summ)
        n3=n3+summ3
    R=int(n3,3)
    if (R%2==0) and R>220:
        res.append(R)
print (min(res))'''
#######################################