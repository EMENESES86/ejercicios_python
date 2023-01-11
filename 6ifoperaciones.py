#Ing. Edison Meneses MSc.
#Ingeniero en Sistemas de Información
#Magister en Sistemas de Información Mención en Inteligencia de Negocios y Analítica Datos Masivos
#tutorias@emenesesdevelopers.com


#Realizar un selector para operaciónes aritméticas
#1. Realizar un menú con las operaciones aritméticas
#2. Seleccionar por el menú que operación voy a realizar, utilizando ingreso por teclado
#3. Indicar qué operación se selecciono
#4. Ingresar num1 y num2 por teclado tomando en cuenta el tipo de dato
#5. Las operaciones se realizarán con el IF ANIDADO
#6. Las operaciones minimas son: SUMA, RESTA, MULT, DIV, POTENCIA

print("1suma")
print("2resta")
print("3mult")
print("4div")
print("5pot")
print("-------------------------------------")
ope = int(input("Seleccione la operacion a realizar: "))
print("-------------------------------------")
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
# num1 =5
# num2 =0
# ope=5

if ope>=1 and ope<=5:
    if ope == 1:
        suma = num1+num2
        print(suma)
    else:
        if ope ==2:
            rest = num1-num2
            print(rest)
        else:
            if ope ==3:
                mult = num1*num2
                print(mult)
            else:
                if ope ==4:
                    if num2==0:
                        print("No existe div para cero")
                    else:
                        div = num1/num2
                        print(div)
                else:
                    if ope==5:
                        pot = num1**num2
                        print(pot)
                    else:
                        print("Algo Salio mal")
else:
    print("No existe esa opcion")
