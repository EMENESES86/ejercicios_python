a = 50
b = 1
c = 8

if a > b:
    print("a>b")
    print(a, "Es mayor que", b)
    
    
if a > b:
    print("a>b")
    print(a, "Es mayor que", b)
else:
    print("b>a")
    print(b, "Es mayor que", a)


if a > b:
    print("a>b")
    print(a, "Es mayor que", b)
    if b < c:
        print("b<c")
        print(b, "Es menor que", c)
    else:
        print("b>c")
        print(b, "Es mayor que", c)
else:
    print("b>a")
    print(b, "Es mayor que", a)