def obwod(a,b,c):
    obwod =a+b+c
    return obwod
def pole(a,b,c):
    p=0.5*(a+b+c)
    pole =(p*(p-a)*(p-b)*(p-c))**0.5 # wzór Herona
    return pole
def jakitrojkat_boki(a,b,c):
    if a==b and b==c:
        return "równoboczny"
    if a==b or a==c or b==c:
        return "równoramienny"
    else:
        return "różnoboczny"
def jakitrojkat_katy(a,b,c):
    if a>b:
        a,b=b,a
    if a>c:
        a,c=c,a
    if b>c:
        b,c=c,b
    if c**2==(a**2+b**2):
        return "prostokatny"
    if c**2 > a ** 2 + b ** 2:
        return "rozwartokatny"
    if c**2<a**2+b**2:
        return "ostrokatny"
