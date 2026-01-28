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