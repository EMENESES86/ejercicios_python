#Ing. Edison Meneses MSc.
#Ingeniero en Sistemas de Información
#Magister en Sistemas de Información mensión inteligencia de negocios y analítica de datos masivos
#tutorias@emenesesdevelopers.com


# A un trabajador le descuentan de su sueldo el 10%, si su sueldo es menor o igual a 1000. 
# por encima de 1000 y hasta 2000 el 5% del adicional, 
# y por encima de 2000 el 3% del adicional. 
# calcular el descuento y sueldo neto que recibe el trabajador dado su sueldo.

#1. sueldo >=0
#2. sueldo<=1000 -0.1
#3. sueldo>1000 y sueldo<=2000 -0.15
#4. sueldo >2000 -0.18
#5. desc?
#6. St?

sueldo = float(input("Ingrese el sueldo: "))

if sueldo>=0:
    if sueldo<=1000:
        desc = sueldo*.1
        St = sueldo-desc
        print("Su sueldo es ", sueldo,"menos el descuento de ",desc,"su sueldo total es de ",St)
    else:
        if sueldo>1000 and sueldo<=2000:
            desc = sueldo*.15
            St = sueldo-desc
            print("Su sueldo es ", sueldo,"menos el descuento de ",desc,"su sueldo total es de ",St)
        else:
            if sueldo>2000:
                desc = sueldo*.18
                St = sueldo-desc
                print("Su sueldo es ", sueldo,"menos el descuento de ",desc,"su sueldo total es de ",St)
            else:
                print("Algo salio mal")
else:
    print("No existe sueldo negativo")

