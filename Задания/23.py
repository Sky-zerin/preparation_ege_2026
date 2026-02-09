'''def f(x,y):
    if x==y:
        return 1
    if x>y:
        return 0
    if x<y:
        return f(x+1,y) + f(x+2,y)
print (f(3,15) + f(3,14))'''
###################################
'''def f(x,y):
    if x==y:
        return 1
    if x<y:
        return 0
    if x>y:
        return f(x-1,y) + f(x//2,y)
print (f(32,11) * f(11,1))'''
###################################
def f(x, y):
    if x == y:
        return 1
    if x < y or x == 24:
        return 0
    return f(x-1, y) + f(x-6, y) + f(x//2, y)

print(f(34, 20) * f(20, 19) * f(19, 6))
