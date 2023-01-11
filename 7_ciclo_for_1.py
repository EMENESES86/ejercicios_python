
#---------------------------EJEMPLO-----------------------------
# for i in [0,1,2]:
#     print("EMENESES ",end=" ")

#---------------------------EJEMPLO-----------------------------
# for i in [0,1,2]:
#     print("ahora i vale ",i,"su cuadrado es ",i**2)

#---------------------------EJEMPLO-----------------------------
# for i in [8,5,2,3]:
#     print("ahora i vale ",i,"su mult por si mismo es ",i*i)

#---------------------------EJEMPLO-----------------------------
# for i in ["EMENESES","DEVELOPERS",1986,"hola mundo"]:
#     print("ahora i vale ",i)

#---------------------------EJEMPLO-----------------------------
# for i in [0,1,2,3,4,5]:
#     print(i,"x",i,"=",i*i)

#---------------------------EJEMPLO-----------------------------
# for x in "EMENESES":
#     print(x)

#---------------------------EJEMPLO-----------------------------
# for a in range(0,11):
#     print("tabla del ",a)
#     for b in range(0,11):
#         print(a,"x",b,"=",a*b)

#---------------------------EJEMPLO-----------------------------
# for i in range(-10,0):
#     print(i*-1)

#---------------------------EJEMPLO-----------------------------
# resto=5%2
# if resto==0:
#     print("El resto es: ",resto,"es numero par")
# else:
#     print("El resto es: ",resto,"es numero impar")
    
#---------------------------EJEMPLO-----------------------------
#Realizar un programa que me liste unicamente los numeros pares partiendo del ingreso por teclado de un numero
# num = int(input("Ingrese el rango: "))

# for i in range(0,num+1):
#     # print(i)
#     resto = i%2
#     if resto == 0:
#         if i==0:
#             print(i,"No esta derterminado el cero como par o impar")
#         else:
#             print("El numero es par",i)
#     else:
#         print("El numero es impar",i)

#---------------------------EJEMPLO-----------------------------
# num = int(input("Ingrese el rango: "))
# for i in range(0,num,2):
#     print(i)
    

#---------------------------EJEMPLO-----------------------------
# x = int(input("Ingrese el inicio: "))
# y = int(input("Ingrese el limite: "))
# if x<=y and x>0 and y>0:    
#     for a in range(x,y+1):
#         print(a,"+",(y-a)+x,"=",a+(y-a)+x)
# else:
#     print("el inicio <= limite, el inicio > 0, el limite>0")
