
print("Automotores Chevrolet")
print("Menú de opciones")
print("1) Verificar el estado de los talleres")
print("2) Salir")
opcion = int(input("Ingrese la opción: "))

while (opcion >=3): 
  print("Recuerde las opciones")
  print("1.- Verificar el estado de los talleres")
  print("2.- Salir")
  opcion = int(input("Ingrese la opción: "))

while (opcion ==1):
  print("Ejecutar caso 1")
  contador_fugas = 0
  talleres = 1
  while (talleres <= 3):
    print("Existe fuga en el taller ", talleres)
    estado = int(input("Ingrese 1) si o 2) no: "))
    if (estado>=3):
        print("Digite bien los numeros")
    elif (estado == 1):
      contador_fugas += 1
    talleres += 1
  if (contador_fugas <= 1):
      print("No se realizara ninguna opcion")
  elif (contador_fugas > 1):
      print("Enviar correo")

  print("1.- Verificar el estado de los talleres")
  print("2.- Salir")
  opcion = int(input("Ingrese la opción: "))

  while (opcion >=3):
    print("Recuerde las opciones")
    print("1.- Verificar el estado de los talleres")
    print("2.- Salir")
    opcion = int(input("Ingrese la opción: "))
print("Muchas gracias por utilizar nuestro sistema")

#AdrianCadena