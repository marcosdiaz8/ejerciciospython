notas = []
while True:
    a = float (input("Ingrese un numero(cero para terminar): "))
    if a != 0:
        notas.append(a)
        promedio = sum(notas)/len(notas)
    else:
        print("El promedio es : ",promedio)