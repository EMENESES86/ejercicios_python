# num1 = 5
# num2 = 3

num1 = float(input("ingrese num1: "))
num2 = float(input("ingrese num2: "))

suma = num1+num2
print("La suma es: ", suma)

resta = num1-num2
print("La resta es: ", resta)

mult = num1*num2
print("La mult es: ", mult)

if num2 == 0:
    print("No existe la div para cero")
else:
    div = num1/num2
    print("La div es: ", div)

if num2 == 0:
    print("No existe la div para cero")
else:
    divint=num1//num2 #parte entera de la divi
    print("La divint es: ",divint)

if num2 == 0:
    print("No existe la div para cero")
else:
    resto=num1%num2
    print("La resto es: ",resto)

potencia = num1**num2
print("La potencia es: ", potencia)
