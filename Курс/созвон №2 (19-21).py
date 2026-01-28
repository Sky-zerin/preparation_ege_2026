def f (k, hod, hod_itog, igrok):
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
        print(k)