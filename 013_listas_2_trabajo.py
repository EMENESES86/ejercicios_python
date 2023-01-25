# Ingresar por teclado la cantidad de valoras que va a contener la lista
# ingresar por teclado los valors que va a tener cada elemento de la lista
# ingresar por teclado el valor a eliminar de la lista
# remover el elemento de la lista

cantidad = int(input("ingrese la cantida de valores: "))
lista=[]
for i in range(1,cantidad+1):
    valor=input("ingrese el valor: ")
    lista.extend([valor])
print("La longitud es ", len(lista))
eliminar=input("Ingrese el valor a eliminar: ")
i=0
while i <= len(lista):
    if eliminar in lista:
        lista.remove(eliminar)
    i+=1
print(lista)