a = int(input("Ingrese un numero,esta app mostrara los n° pares entre 2 y el n° introducido: "))
lista = []
if a>=2:
    for i in range(2,a+1):
        if i%2==0:
            lista.append(i)
            print(lista)
else:
    a<2
    print("error")
