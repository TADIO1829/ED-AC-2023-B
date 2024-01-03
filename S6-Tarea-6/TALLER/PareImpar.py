#PareImpar

numero=1
par=0
impar=0

while numero!=0:
    numero=int(input("Ingrese el numero(digite 0 para salir): "))
    if numero>0:
        if numero%2==0:
            par=par+1
        else:
            impar=impar+1

print("El total de numeros pares es: ",par)
print("El total de numeros impares es: ",impar)
