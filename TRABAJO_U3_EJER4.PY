energia = 100
tiempo = 12
cerraduras = 0
alarma = False
codigo = ""
cierre_forzado = 0

# nombre
nombre = input("Ingrese su nombre: ").lower().strip()
while not nombre.isalpha():
    print("Error: Debe ingresar un nombre que contenga solo letras")
    nombre = input("Ingrese su nombre: ").lower().strip()
while energia > 0 and tiempo > 0 and cerraduras < 3:
    print(f"Energia: {energia}, Tiempo: {tiempo}, Cerraduras: {cerraduras}. Alarma: {alarma}")
    
    print("Menu:")
    print("1. Forzar Cerradura") 
    print("2. Hackear Panel.")
    print("3. Descansar.")
    opcionstr = input("Seleccione una de las opciones dadas:  ").strip()
    while not opcionstr.isdigit or int(opcionstr) not in range(1,4):
        print("Error: Ingrese el numero de opcion valido")
        opcionstr = input("Seleccione una de las opciones dadas:  ").strip()
        continue
    opcionint= int(opcionstr)
    if opcionint == 1:
        energia -=20
        tiempo -=2
        cierre_forzado +=1
        if energia < 40:
            print("Hay riesgo de alarma")
            print("Tenes que elegir un numero del 1 al 3")
            numeroelegidostr=input("Ingresa el numero que deseas: ").strip()
            while not numeroelegidostr.isdigit or int(numeroelegidostr) not in range(1,4):
                print("Error: Ingrese un numero del 1 al 3")
                numeroelegidostr=input("Ingresa el numero que deseas: ").strip()
                continue
            intnumeroelegido= int(numeroelegidostr)
            if  intnumeroelegido == 3:
                alarma = True
                print("Estas Bloqueado, perdiste!!")
                break
            if intnumeroelegido != 3:
                print("Abriste una cerradura!!")
                cerraduras +=1
    elif opcionint == 2:
        energia -=10
        tiempo -=3
        cierre_forzado=0
        print("Hackeando...")
        for i in range(4):
            codigo += "A"
        if len(codigo) >= 8:
            if cerraduras < 3:
                cerraduras += 1
                print("Hackeo exitoso")
    elif opcionint == 3:
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        racha = 0
        if alarma:
            energia -= 10
if cerraduras == 3:
    print("GANASTE")
elif alarma == True and tiempo <= 3:
    print("PERDISTE POR BLOQUEO")
else:
    print("PERDISTE")





            

   