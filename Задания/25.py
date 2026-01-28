#1_вариант решения
'''for i in range (2321,10**8, 2321):
    s=str(i)
    if s[0]=='1' and s[-1]=='6' and s[-2]=='7' and s[-5]=='2':
        print(i,i//2321)'''
#2_вариант решения
'''from fnmatch import *
for i in range (2321,10**8, 2321):
    if fnmatch(str(i),'1*2??76'):
        print(i,i//2321)'''
#################################
'''from fnmatch import*
for i in range (2024,10**8,2024):
    if fnmatch(str(i),'1?4*784'):
        print (i,i//2024)'''
#################################
'''from fnmatch import*
for i in range (31,10**9,31):
    if fnmatch(str(i), '12345?7?8'):
        print(i,i//31)'''
#################################
'''from fnmatch import*
for i in range (137,10**9,137):
    if fnmatch(str(i), '1234*7?8'):
        print(i,i//137)'''
#################################
'''from fnmatch import*
for i in range (17,10**9):
    if i%17==0 and i%1991==0 and fnmatch(str(i), '2*1?71'):
        print(i,i//1991)'''
#################################
'''for i in range (2027,10**15,2027):
    s=str(i)
    if s[0]=='6' and s[2]=='2' and s[3]=='8' and s[5]=='5' and s[6]=='5' and s[-1]=='1' and int((s[1]))%2==0 and int((s[4]))%2==0:
        print(i,i//2027)'''
#################################