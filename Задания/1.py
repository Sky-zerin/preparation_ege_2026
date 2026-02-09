'''from itertools import*
table = "2347 16 158 157 348 278 146 356".split()
draw = "AB BE EH HC CF FD AD DB DG HG GE".split()
for t in permutations("ABCDEFGH"):
    if all(str(t.index(x)+1) in table[t.index(y)] for x,y in draw):
        print(t)'''
#######################################
'''from itertools import*
tb='247 148 578 126 38 47 136 235'.split()
dr='ab bh hf fd dc ec ae eg gc gf ah'.split()
for s in permutations('abcdefgh'):
    if all(str(s.index(x)+1) in tb [s.index(y)] for x,y in dr):
        print(s)'''
#######################################
'''from itertools import*
table ='28 1467 59 29 37 289 259 16 3467'.split()
draw ='АБ БВ ВЕ ЕК КИ ИЖ ЖГ АГ ГД ДЕ ЖЕ ГВ'.split()
for t in permutations('АБВГДЕЖИК'):
    if all(str(t.index(x)+1) in table [t.index(y)] for x,y in draw):
        print(t)'''
#######################################
'''from itertools import *
tb ="367 357 12467 356 24 134 123".split()
dr="ad ag ae ef eg eb ec bg bc cf df".split()
for t in permutations("abcdefg"):
    if all(str(t.index(x)+1) in tb [t.index(y)] for x,y in dr):
        print(t)'''
#######################################
'''from itertools import*
tb='467 345 27 126 267 145 135'.split()
dr='AB BG GE EF FA AD FD DC EC BC'.split()
for t in permutations('ABCDEFG'):
    if all(str(t.index(x)+1) in tb [t.index(y)] for x,y in dr):
        print(t)'''
#######################################