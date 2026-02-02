def f(k1,k2,hod,hod_itog,igrok):
    if hod>hod_itog:
        return False
    if k1+k2<=40:
        if hod%2==igrok:
            return True
        else:
            return False
    if (hod+1)%2==igrok:
        return f(k1-1,k2,hod+1,hod_itog,igrok) and f(k1,k2-1,hod+1,hod_itog,igrok) and f(k1//2,k2,hod+1,hod_itog,igrok) and f(k1,k2//2,hod+1,hod_itog,igrok)
    else:
        f(k1-1,k2,hod+1,hod_itog,igrok) or f(k1,k2-1,hod+1,hod_itog,igrok) or f(k1//2,k2,hod+1,hod_itog,igrok) or f(k1,k2//2,hod+1,hod_itog,igrok)
for s in range (1,78):
    if f(k1=20,k2=s,hod=0,hod_itog=2,igrok=1)==True:
        print(s)