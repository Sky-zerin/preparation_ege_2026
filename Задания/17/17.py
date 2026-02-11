'''f=open ("17_38951.txt")
s=[int(i) for i in f]
k=0
summ=0
for i in range (len(s)-1):
    if s[i] %3==0 or s[i+1]%3==0:
        if (s[i] + s[i+1]) %5 ==0:
            k+=1
            summ=max(summ,s[i]+s[i+1])
print(k,summ)'''
#################
'''f=open("17_39762.txt")
s=[int(i) for i in f]
k=0
summ=0
for i in range (len(s)-1):
    if (s[i] * s[i+1])%15==0:
        if (s[i] + s[i+1]) %7 ==0:
            k+=1
            summ=max(summ,s[i]+s[i+1])
print(k,summ)'''
#################
'''f=open('69927.txt')
s=[int(i) for i in f]
k=0
summ=0
Z=0
for i in range (len(s)):
    if abs(s[i])%32==0:
        k+=1
for i in range (len(s)-1):
    if (s[i]) <0 or s[i+1]<0:
        if s[i] + s[i+1] < k:
            Z+=1
            summ=max(summ,s[i]+s[i+1])
print(Z,summ)'''
#################
'''f=open('17_39764.txt')
s=[int(i) for i in f]
k=0
summ=0
for i in range (len(s)-2):
    s1=sorted([s[i],s[i+1],s[i+2]])
    if s1[2]**2==s1[0]**2+s1[1]**2:
        k+=1
        summ=max(summ,s[i]+s[i+1]+s[i+2])
print(k,summ)'''
#################
'''f=open("17_68518.txt")
s=[int(i) for i in f]
k=0
summ=0
for i in range (len(s)-1):
    if (s[i]%(min(int(s%19==0))))==0 or (s[i+1]%(min(int(s%19==0))))==0:
        k+=1
        summ=max(summ,s[i]+s[i+1])
print(k,summ)'''
#################
'''f=open("17_46975.txt")
s=[int(i) for i in f]
s_chet=sum([x for x in s if x % 2 == 0])
k=0
summ=0
for i in range (len(s)-1):
    if (s[i]%3==0 and s[i+1]<s_chet) or (s[i+1]%3==0 and s[i]<s_chet):
        k+=1
        summ=max(summ,s[i]+s[i+1])
print(k,summ)'''
#################
'''f=open("17_47014.txt")
s=[int(i) for i in f]
s_nechet=sum([x for x in s if x % 2 == 1])
k=0
summ=0
for i in range (len(s)-1):
    if (s[i] % 5 == 0 and s[i + 1] < s_nechet) or (s[i + 1] % 5 == 0 and s[i] < s_nechet):
        k += 1
        summ = max(summ, s[i] + s[i + 1])
print(k, summ)'''
#################
'''f=open("17_37362.txt")
s=[int(i) for i in f]
k=0
summ=0
for i in range (len(s)-1):
    for j in range(i+1, len(s)-1):
        if ((s[i] + s[j]) % 80 == 0) and (s[i] % 50 == 0 or s[j] % 50 == 0):
            k+=1
            summ = max(summ, s[i] + s[j])
print(k, summ)'''
#################
'''f=open('17_1993.txt')
s=[int(i) for i in f]
k=0
summ=0
for i in range (len(s)-1):
    if abs(s[i]+s[i+1])%3==0 and abs(s[i]+s[i+1])%6!=0 and str(s[i]*s[i+1])[-1]=='8':
        k+=1
        summ=max(summ,s[i]+s[i+1])
print(k, summ)'''
#################
'''f=open('17_12450.txt')
s=[int(i) for i in f]
k=0
summ=0
a52=[]
for x in range (len(s)):
    if s[x]%52==0:
        a52.append(s[x])
for i in range (len(s)-2):
    if s[i]%113+s[i+1]%113+s[i+2]%113==min(a52):
        k+=1
        summ=max(summ,s[i]+s[i+1]+s[i+2])
print(k,summ)'''
#################
'''f=open('17_23757.txt')
s=[int(i) for i in f]
k=0
summ=0
a_de=[]
for x in range (len(s)):
    if s[x]>=10 and s[x]<=99:
        a_de.append(s[x])
for i in range (len(s)-1):
     if (s[i]+s[i+1])%min(a_de)==0 and (((s[i]>=10 and s[i]<=99) and (s[i+1]<10 or s[i+1]>99)) or ((s[i+1]>=10 and s[i+1]<=99) and (s[i]<10 or s[i]>99))):
         k+=1
         summ=max(summ,s[i]+s[i+1])
print(k,summ)'''
#################
'''f=open('17.txt')
s=[int(i) for i in f]
mins=min(s)
k=0
summ=0
for i in range (len(s)-1):
    if s[i]%22 == mins or s[i+1]%22 == mins:
        k+=1
        summ=max(summ,s[i]+s[i+1])
print(k,summ)'''
#################
'''f=open('17.txt')
s=[int(i) for i in f]
k=0
summ=0
number = 20001
for i in range (len(s)):
    if str(s[i])[-1]=='5':
        if 99<abs(s[i])<1000:
            number=min(number,s[i])
for i in range (len(s)-1):
    if ((999<abs(s[i])<1000) and not(999<abs(s[i+1])<1000)) or (not(999<abs(s[i])<1000) and not(999<abs(s[i+1]))):
        if (s[i]**2 + s[i+1]**2)%number==0:
            k+=1
            summ=max(summ,s[i]+s[i+1])
print(k,summ)'''
#################
'''f=open('17.txt')
s=[int(i) for i in f]
k=0
summ=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
maxe=[int(x) for x in s if len(str(abs(x)))==5 and abs(x)%100==43]
maxe1=max(maxe)
for i in range (len(s)-2):
    if s[i] in maxe or s[i+1] in maxe or s[i+2] in maxe:
        if s[i]**2 + s[i+1]**2 + s[i+2]**2 <=maxe1**2:
            k+=1
            summ=min(summ,s[i]**2+s[i+1]**2+s[i+2]**2)
print(k,summ)'''
#################