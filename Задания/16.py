#############################
'''def f(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return f(n-1)*n-2*f(n-2)
print(f(6))'''
#############################
'''import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n>=2:
        return 3*f(n-1)-n
    if n==1:
        return 2
print((f(2025)-f(2023)-1)//3**2022)'''
#############################
'''import sys
sys.setrecursionlimit(10000)
def f(n):
    if n>=2025:
        return n
    if n<2025:
        return n+3+f(n+3)
print(f(2018)-f(2022))'''
#############################