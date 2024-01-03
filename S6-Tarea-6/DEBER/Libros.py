#Libros

print("Ejercicio 6: Conteo de dígitos numéricos en títulos de libros")

lineascompletas = 0
digitostotales = 0
print(" Use * para acabar y muestre las lineas completas")
print(" Use / para ver los dígitos númericos de un título")
while True:
    titulo=input("Libro: ")

    if titulo == "*":
        break
    elif titulo == "/":
        print("Línea completa. Aparecen", digitostotales, "dígitos numéricos.")
        lineascompletas += 1
        digitostotales = 0
    else:
        digitostotales += sum(1 for caracter in titulo if caracter.isdigit())
print("Fin. Se leyeron", lineascompletas, "líneas completas.")