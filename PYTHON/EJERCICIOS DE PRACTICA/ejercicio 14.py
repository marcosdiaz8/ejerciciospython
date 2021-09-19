nombre = (input("Ingrese su nombre completo: "))
lista1 = []
lista2 = []
lista3 = []
while True:
    if nombre:
        lista1.append(nombre.upper())
        print(lista1*3)
        lista2.append(nombre.title())
        print(lista2*3)
        lista3.append(nombre.lower())
        print(lista3*3)
        break
    else:
        print("Error.")