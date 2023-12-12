
print("****MENU****")
nom=input("Ingrese su nombre: ")
ced=input("Ingrese su numero de cedula: ")
corr=input("Ingrese su correo electronico: ")
print("Le ofrecemos los siguientes tipos de Hamburguesas:","\n","1)Sencillas","\n","2)Dobles","\n","3)Triples")
tipo=int(input("Elija el tipo de hamburguesa que desea: "))


if tipo==1:
        precio=1.5
        cant=int(input("Ingrese la cantidad deseada: "))
        paga=precio*cant
        print("Por su compra debe pagar: ",paga)
        print("Seleccione el tipo de pago:","\n","1)Efectivo","\n","2)Tarjeta de credito")
        pago=int(input("1 o 2: "))
        if pago==1:
            iva=0
            total=paga+iva
            print("Su pago es en efectivo, lo cual no conlleva recarga y el total a pagar es: ",total)    
            print(nom,"Muchas gracias por su compra, vuelva pronto","\n","La factura sera enviada a su correo")

        if pago==2:
                iva=0.05
                total=paga+paga*iva
                print ("Su pago es con tarjeta de credito lo cual se le agrega un 5%","al pago :",total)
                print(nom,"Muchas gracias por su compra, vuelva pronto","\n","La factura sera enviada a su correo")
        else:
                print("No disponemos ese tipo de pago")   
    
if tipo==2:
        precio=2.5
        cant=int(input("Ingrese la cantidad deseada: "))
        paga=precio*cant
        print("Por su compra debe pagar: ",paga)
        print("Seleccione el tipo de pago:","\n","1)Efectivo","\n","2)Tarjeta de credito")
        pago=int(input("1 o 2: "))
        if pago==1:
            iva=0
            total=paga+iva
            print("Su pago es en efectivo, lo cual no conlleva recarga y el total a pagar es: ",total)    
            print(nom,"Muchas gracias por su compra, vuelva pronto","\n","La factura sera enviada a su correo")
        if pago==2:
                iva=0.05
                total=paga+paga+iva
                print ("Su pago es con tarjeta de credito lo cual se le agrega un 5%","al pago :",total)
                print(nom,"Muchas gracias por su compra, vuelva pronto","\n","La factura sera enviada a su correo")
        else:
                print("No disponemos ese tipo de pago")   
if tipo==3:
        precio=3.25
        cant=int(input("Ingrese la cantidad deseada: "))
        paga=precio*cant
        print("Por su compra debe pagar: ",paga)
        print("Seleccione el tipo de pago:","\n","1)Efectivo","\n","2)Tarjeta de credito")
        pago=int(input("1 o 2: "))
        if pago==1:
            iva=0
            total=paga+iva
            print("Su pago es en efectivo, lo cual no conlleva recarga y el total a pagar es: ",total)    
            print(nom,"Muchas gracias por su compra, vuelva pronto","\n","La factura sera enviada a su correo")

        if pago==2:
                iva=0.05
                total=paga+paga*iva
                print ("Su pago es con tarjeta de credito lo cual se le agrega un 5%","al pago :",total)
                print(nom,"Muchas gracias por su compra, vuelva pronto","\n","La factura sera enviada a su correo")
        else:
                print("No disponemos ese tipo de pago")   
if tipo>3:
     print ("No disponemos de ese tipo de hamburguesa")
    #Adrian Cadena