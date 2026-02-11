#############################
'''from itertools import *
alf='АОУ'
k=0
for x in product('АОУ', repeat = 5):
    k+=1
    print(k,x)'''
#############################
'''from itertools import *
alf='УЧЕНИК'
k=0
for x in product('УЧЕНИК', repeat =3):
    s=''.join(x)
    k+=1
    if s[0]=='К':
        print(k,s)'''
#############################
'''alf='ЕГЭ'
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s=x1+x2+x3+x4+x5
                    if s[0] in 'ЕЭ':
                        k+=1
                        print(k)'''
#############################
'''alf='ЛЕТО'
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                s=x1+x2+x3+x4
                if s[0] in 'ЛТ':
                    k+=1
print(k)'''
#############################
'''alf='СЛОН'
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    s=x1+x2+x3+x4+x5
                    if s.count('С')==1:
                        k+=1
print(k)'''
#############################
'''alf='ДЕЖЗ'
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                s=x1+x2+x3+x4
                if s.count('Д')==1:
                    k+=1
print(k)'''
#############################
'''alf = 'ЛЕМУР'
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                s=x1+x2+x3+x4
                if s[0] in 'М' and s.count('М')==1:
                    k+=1
print(k)'''
#############################
'''alf = 'ВИШНЯ'
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        s=x1+x2+x3+x4+x5+x6
                        if s.count('В')<=1 and  s[0] not in 'Ш' and s[-1] not in 'ИЯ':
                            k+=1
print(k)'''
#############################
'''from itertools import *
alf='012345678'
k=0
for x in product(alf, repeat=5):
    s=''.join(x)
    if s[0] != '0':
        s=s.replace('0','*')
        s=s.replace('2','*')
        s=s.replace('4','*')
        s=s.replace('6','*')
        s=s.replace('8','*')
        if s.count('1')==1 and '1*' not in s and '*1' not in s:
            k+=1
print(k)'''
#############################
'''from itertools import *
alf ='АЕЛРСТ'
k=0
for x in product (alf, repeat=5):
    s=''.join(x)
    if s[0] not in 'АСТ' and s.count('Л')==2 and 'ЛЛ' not in s:
        k+=1
        print(k,s)'''
#############################
'''from itertools import*
alf='012345678'
k=0
for x in product(alf, repeat=5):
    s=''.join(x)
    if s[0] not in '01357':
        if s[4] not in '12':
            if s.count('8')>=2:
                k+=1
                print(k,s)'''
#############################
'''from itertools import*
alf='ИГОРЬ'
k=0
for x in product(alf,repeat=8):
    s=''.join(x)
    if s.count('Ь')==1 and s.count('О')==1:
        if s[0] not in 'Ь':
            k+=1
print(k)'''
#############################
'''from itertools import*
alf='ВИШНЯ'
k=0
for x in product(alf, repeat=5):
    s=''.join(x)
    if s.count('В')<=1:
        if s[0] not in 'Ш':
            if s[4] not in 'ИЯ':
                k+=1
                print(k)'''
#############################
'''from itertools import*
alf='АМПТЬЯ'
k=0
for x in product(alf,repeat=5):
    s=''.join(x)
    k += 1
    if s.count('Ь')==0:
        if s.count('Я')==2:
            print(k,s)'''
#############################