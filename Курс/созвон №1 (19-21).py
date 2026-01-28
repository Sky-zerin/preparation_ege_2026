def f(s, hod, hod_itog, igrok):
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
        print(s)