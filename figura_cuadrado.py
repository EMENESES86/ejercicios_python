#Ing. Edison Meneses MSc.
#Ingeniero en Sistemas de Información
#Magister en Sistemas de Información Mención en Inteligencia de Negocios y Analítica Datos Masivos
#tutorias@emenesesdevelopers.com

#Ejercicio de cuadrado con altura, ancho y simbolo
altura=int(input("Introduce la altura: "))
anchura=int(input("Introduce la anchura: "))
simbolo=(input("Ingresa un simbolo o letra: "))


# for x in range(1):
print(" # "*anchura)
for y in range(altura-2):
    g=anchura-2#numero de guiones
    print(" # "+((" "+simbolo+" ")*g)+" # ")
print(" # "*anchura)


 #  #  #  #  #  #
 #  *  *  *  *  #
 #  *  *  *  *  #
 #  *  *  *  *  #
 #  #  #  #  #  #