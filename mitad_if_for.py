num = int(input("Ingrese el numero par: "))

mitad = num/2
print('\nLa mitad de',num,"es",mitad,'\n')

par = num%2
if par==0:  
    if num>=0:  
        for i in range(0,num+1):
            if i>mitad:
                print(i,"Meneses")
            else:
                if i<mitad:
                    print(i,"Edison")
                else:
                    print(i,"*******Mitad*********")
    else:
        for i in range(num,0+1):
            if i>mitad:
                print(i,"Meneses")
            else:
                if i<mitad:
                    print(i,"Edison")
                else:
                    print(i,"*******Mitad*********")
else:
    print("No es num par")