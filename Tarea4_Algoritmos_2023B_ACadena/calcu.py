import math
print("***CALCULADORA***")
num1=int(input("Ingrese el primer numero: "))
num2=int(input ("Ingrese el segundo numero:"))
print("1) Sumar","\n","2) Restar","\n","3) Multiplicar","\n","4) Dividir","\n","5) Modulo","\n","6) Potencia")
co=int(input("Que desea hacer: " ))
match(co):
    case 1:
        suma=num1+num2
        print("La suma de los numeros es igual a : ",suma)
    case 2:
        resta=num1-num2
        print("La resta de los numeros es igual a : ",resta)
    case 3:
        multi=num1*num2
        print("La multiplicacion de los numeros es igual a : ",multi)
    case 4:
        if num2!=0:
            div=num1/num2
            print("La division de los 2 numeros es igual a:  ",div)
        else:
            print("No se puede dividir para cero")
    case 5:
        if num2!=0:
            mod=num1%num2
            print("El modulo entre los dos numero es: ",mod)
        else:
            print("No se puede sacar el modulo a cero")
    case 6:
        pot=pow(num1,num2)
        print ("La potencia entre los 2 numero es igual a : ",pot)
    case other:
        print("Ingrese un numero valido")
#Adrian Cadena
