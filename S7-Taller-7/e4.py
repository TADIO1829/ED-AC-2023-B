print("Bienvenido a la escuela Fe y Alegria")
ncali= 4
total= 0.0
for i in range(1,5):
  print(f"Ingresa la calificación {i}: ",end="")
  calificaciones = float(input())
  total += calificaciones
print("La suma de calificaciones es: ",total)
promedio = total/ncali
print("El promedio de las calificaciones es: ",promedio)
if promedio >=14:
  print("Aprobado")
elif (9 <= promedio <= 13):
  print("Supletorio")
elif promedio <= 8:
  print("Rechazado")

  #AdrianCadena