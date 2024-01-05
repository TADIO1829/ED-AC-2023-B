
numero = int(input("Ingrese un número entero positivo en el intervalo de 10-100: "))

while numero<0 or numero ==0 :
  print("número debe ser un entero positivo")
  numero = int(input("Ingrese un número entero positivo en el intervalo de 10-100: "))

if 10<=numero<=100:
  print("El número si pertenece al rango")
else:
  print("El número no pertenece al rango")

  #AdrianCadena
