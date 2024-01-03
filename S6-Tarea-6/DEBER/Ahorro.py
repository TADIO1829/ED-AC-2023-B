print ("**Bienvenido**")
ahorro =float (input ("Ingrese la cantidad de dinero que desea ahorrar: "))
sumaahorro = 0

while ahorro < 0:
  if ahorro < 0:
      print ("No puede ahorrar cantidades negativas")
      ahorro =float (input ("Ingrese la cantidad de dinero que desea ahorrar: "))
while sumaahorro<ahorro:
    dinero =float (input ("Ingrese el valor de su deposito: "))
    if dinero < 0:
        print ("No puede ingresar cantidades negativas")
    else:
        sumaahorro = sumaahorro + dinero
        print(sumaahorro, " + ", dinero, " = ", sumaahorro)
print ("Ha cumplido con su meta")
#Adrian Cadena 