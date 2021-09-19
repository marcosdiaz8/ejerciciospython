a = int(input("Ingrese un numero: "))
b = 1
if a>=0:
    for i in range(1,a+1):
        b=b*i
print("El factoria de tu numero es: ",b)