a = int(input("Ingrese un numero: "))
lista = []
while True:
    if a<0:
        print("El programa termino.")
        break
    else:
        a = int(input("Ingrese un numero: "))
        lista.append(a)
print("El numero mas grande fue: ",max(lista))