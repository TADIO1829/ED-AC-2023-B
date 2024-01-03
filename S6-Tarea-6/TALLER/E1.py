
cantidad=int(input("INGRESE LA CANTIDAD DE NOTAS QUE VA A USAR: "))
numero=1
suma=0
x=0
while x !=cantidad:
    x=x+1
    numero=int(input("Ingrese un numero"))
    if numero>0:
        suma=suma+numero



promedio=suma/cantidad
print("El promedio es igual a : ",promedio)
