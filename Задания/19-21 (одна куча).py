''''def f(s,hod, hod_itog, igrok):
    if hod > hod_itog:
        return False
    if s<=60:
        if hod%2==igrok:
            return True
        else:
            return False
    if(hod+1)%2==igrok:
        return f(s-3,hod+1, hod_itog, igrok) or f(s-5,hod+1, hod_itog, igrok) or f(s//4,hod+1, hod_itog, igrok)
    else:
        return f(s-3,hod+1, hod_itog, igrok) and f(s-5,hod+1, hod_itog, igrok) and f(s//4,hod+1, hod_itog, igrok)
for s in range (100,61):
    if f(s,hod=0, hod_itog=4, igrok=1)==True:
        print(s)'''
##################################
'''def f(s, hod, hod_itog,igrok):
    if hod > hod_itog:
        return False
    if s<=87:
        if hod%2==igrok:
            return True
        else:
            return False
    if (hod+1)%2== igrok:
        return f(s-2, hod+1, hod_itog,igrok) or f(s//2, hod+1, hod_itog,igrok)
    else:
        return f(s-2, hod+1, hod_itog,igrok) and f(s//2, hod+1, hod_itog,igrok)
for s in range (88,2000):
    if f(s, hod=0, hod_itog=2,igrok=0)==False and f(s, hod=0, hod_itog=4,igrok=0)==True:
        print(s)'''
##################################
'''def f(s,hod,hod_itog,igrok):
    if hod>hod_itog:
        return False
    if s>=27:
        if hod%2==igrok:
            return True
        else:
            return False
    if (hod+1)%2==igrok:
        return f(s+1,hod+1,hod_itog,igrok) or f(s+2,hod+1,hod_itog,igrok) or f(s*2,hod+1,hod_itog,igrok)
    else:
        return f(s + 1, hod + 1, hod_itog, igrok) and f(s + 2, hod + 1, hod_itog, igrok) and f(s * 2, hod + 1, hod_itog,igrok)
for s in range (1,27):
    if f(s,hod=0,hod_itog=4,igrok=0)==True and f(s,hod=0,hod_itog=2,igrok=0)==False:
        print(s)'''
##################################
'''def f (k, hod, hod_itog, igrok):
    if hod>hod_itog:
        return False
    if k>=45:
        if k<112:
            if hod%2==igrok:
                return True
            else:
                return False
        else:
            if hod%2!=igrok:
                return True
    if (hod+1)%2==igrok:
        return f(k+1, hod+1, hod_itog, igrok) or f(k+2, hod+1, hod_itog, igrok) or f(k+3, hod+1, hod_itog, igrok) or f(k*2, hod+1, hod_itog, igrok)
    else:
        return f(k+1, hod+1, hod_itog, igrok) and f(k+2, hod+1, hod_itog, igrok) and f(k+3, hod+1, hod_itog, igrok) and f(k*2, hod+1, hod_itog, igrok)
for k in range (1,34):
    if f(k, hod=0, hod_itog=4, igrok=0)==True:
        print(k)'''
##################################
'''def f(s, hod, hod_itog, igrok):
    if hod>hod_itog:
        return False
    if s>=29:
        if hod%2==igrok:
            return True
        else:
            return False
    if(hod+1)%2==igrok:
        return f(s+1, hod+1, hod_itog, igrok) or f(s*2, hod+1, hod_itog, igrok)
    else:
        return f(s+1, hod+1, hod_itog, igrok) and f(s*2, hod+1, hod_itog, igrok)
for s in range (1,29):
    if f(s, hod=0, hod_itog=2, igrok=0)==True:
        print(s)'''
##################################
'''def f(s,hod,hod_itog,igrok):
    if hod>hod_itog:
        return False
    if s>=97:
        if hod%2==igrok:
            return True
        else:
            return False
    if (hod+1)%2==igrok:
        return f(s+3,hod+1,hod_itog,igrok) or f(s+5,hod+1,hod_itog,igrok) or f(s*3,hod+1,hod_itog,igrok)
    else:
        return f(s + 3, hod + 1, hod_itog, igrok) and f(s + 5, hod + 1, hod_itog, igrok) and f(s * 3, hod + 1, hod_itog,igrok)
for s in range (1,97):
    if f(s,hod=0,hod_itog=2,igrok=0)==False and f(s,hod=0,hod_itog=4,igrok=0)==True:
        print(s)'''
##################################