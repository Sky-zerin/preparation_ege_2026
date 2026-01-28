'''def f(s,hod, hod_itog, igrok):
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