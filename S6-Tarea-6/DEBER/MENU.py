#MENU

print("Ejercicio 3: Menu")
menu= 0
while menu != 3:
    print ("---Bienvenido---")
    print ("1. Comenzar programa")
    print ("2. Imprimir Listado")
    print ("3. Finalizar programa")
    menu = int (input ("Ingresa tu seleccion: "))
    if menu != 1 and menu != 2 and menu != 3:
        print ("Elija una opcion valida")
    elif menu == 1:
        print ("Inicializando programa")
    elif menu== 2:
        print ("a,b,c,d,e,f,g,h,i,j,k")
