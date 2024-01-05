print(" Bienvenido a Etafashion")
prendasVestir = int(input("Ingrese el número de prendas: "))
while prendasVestir<=0:
  print("Debe ingresar un número valido de prendas")
  prendasVestir = int(input("Ingrese el número de prendas: "))

compraTotal = float(input("Ingrese el total de la compra: "))

valorFinal=0.0
while compraTotal<=0:
  print("Debe ingresar el total real")
  compraTotal = int(input("Ingrese el total de las compras: "))

compraTotal = float(input("Ingrese el total de la compra: "))
if prendasVestir>20:
  valorFinal = compraTotal + (compraTotal*0.10)
  print("El valor a pagar es de: ",valorFinal)
elif 10<=prendasVestir<=20:
  valorFinal = compraTotal + (compraTotal*0.05)
  print("El valor a pagar es de: ",valorFinal)
elif prendasVestir<=9:
  print("El valor a pagar es de: ",compraTotal)

#AdrianCadena