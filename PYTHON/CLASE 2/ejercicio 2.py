lista = []

while True:
    a = int(input("Ingrese un numero: "))
    if a > 0:
        lista.append(a)
    else:
        print("El numero mas grande de tu lista es:", (max(lista)) )
        break
print("fin pibe")