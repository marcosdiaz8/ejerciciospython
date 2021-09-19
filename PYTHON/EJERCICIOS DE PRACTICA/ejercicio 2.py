print("Hola,en los siguientes espacios ingrese los valores solicitados:")
personaA = int(input("Ingrese la edad de la persona 1: "))
personaB = int(input("Ingrese la edad de la persona 2: "))
if personaA > personaB:
    print("La persona A es mayor")
elif personaA == personaB:
    print("Las dos personas tienen la misma edad")
else:
    print("La persona B es mayor")