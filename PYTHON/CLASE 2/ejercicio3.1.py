notas = []

while True:
    a = float(input("Ingrese un numero: "))
    if a != 0:
        notas.append(a)
        sum(notas)/len(notas)
        promedio = sum(notas)/len(notas)
    else:
        print("El promedio es:",promedio)