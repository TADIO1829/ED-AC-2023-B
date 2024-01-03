#COMPRA
suma = 0
numero = 1
contador = 0

while numero != 0:
   numero = float (input ("Ingrese el valor de su compra: "))
   print ("Ingrese 0 para finalizar")
   suma = suma + numero
   contador =contador +1
   print (suma)
   
if suma >= 1000:
    respuesta = suma - (suma *0.1)
    print ("El total a pagar es de: ",respuesta)
else:
    print ("El total a pagar es de: ",suma)
#Adrian Cadena