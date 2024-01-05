
numero = int (input("Ingrese el numero que desea: "))
suma=0
suma_formato=""
if (numero<=0):
    print("Recuerde que el numero que dijite debe ser mayor que 0.")
else:
    for m in range(1, numero+1):
         print(m)
         if(m%2==0):
             suma+=m
             
print(f'La suma de los numeros pares es: {suma}')

#AdrianCadena