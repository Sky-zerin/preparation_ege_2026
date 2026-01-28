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