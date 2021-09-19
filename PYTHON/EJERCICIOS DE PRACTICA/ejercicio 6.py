while True:
    a = float(input("Ingrese una nota: "))
    if a < 5:
        print("Suspendido")
    elif a >= 5 or a < 7:
        print("Aprobado")
    elif a >= 7 or a <9:
        print("Notable")
    elif a > 9 or a < 10:
        print("Sobresaliente")
    elif a==10:
        print("Matricula de Honor")
    break