#Ing. Edison Meneses MSc.
#Ingeniero en Sistemas de Información
#Magister en Sistemas de Información Mención en Inteligencia de Negocios y Analítica Datos Masivos
#tutorias@emenesesdevelopers.com

a = 50
b = 1
c = 8

#if simple
if a > b:
    print("a>b")
    print(a, "Es mayor que", b)
    
#if doble
if a > b:
    print("a>b")
    print(a, "Es mayor que", b)
else:
    print("b>a")
    print(b, "Es mayor que", a)

# print("-----elif------")
if a>b:
    print("Verdadero", a , "es >", b)
elif a==b:
    print(a, "es igual a ", b)
elif b>a:
    print(b, 'es mayor que', a)
else:
    print("algo salio mal")

#if compuesto
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