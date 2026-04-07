nombre = input("Ingrese el nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Ingrese el nombre del Gladiador: ")

vidajugador = 100        
vidaenemigo = 100        
pociones = 3              
ataque_pesado = 15        
ataque_enemigo = 12       
turno_jugador = True      

while vidajugador > 0 and vidaenemigo > 0:
    if turno_jugador:
        print(f"nombre: {nombre}")
        print(f"Vida del jugador: {vidajugador}")
        print(f"Pociones disponibles: {pociones}")
        print("--------------------------------")
        print(f"Vida del Enemigo: {vidaenemigo}")
        print("--------------------------------")
        print("Menu:")
        print("1: Ataque Pesado.")
        print("2. Rafaga Veloz")
        print("3. Curar")
        print("---------------------------------")
        opcionstr = input("Seleccione una de las opciones dadas:  ").strip()
        while not opcionstr.isdigit or int(opcionstr) not in range(1,4):
            print("Error: Ingrese el numero de opcion valido")
            opcionstr = input("Seleccione una de las opciones dadas:  ").strip()
            continue
        opcionint= int(opcionstr)
        if opcionint == 1:
            if vidaenemigo < 20:
                golpecritico= ataque_pesado * 1.5
                vidaenemigo-=float(golpecritico)
                print(f"!Atacaste al enemigo por {golpecritico} puntos de daño")
            else:
                vidaenemigo-= ataque_pesado

                print(f"¡Atacaste al enemigo por {ataque_pesado} puntos de daño!")
        
        elif opcionint ==2:
            for i in range(3):
                ataquerafaga=5
                vidaenemigo-=ataquerafaga
                print(f"GOLPE CONECTADO POR {ataquerafaga} puntos de daño")

        elif opcionint==3:
            if pociones > 0:
                vidajugador +=30
                if vidajugador > 100:
                    vidajugador=100
                pociones -= 1
                print(f"Usaste una pocion, tu vida ahora es {vidajugador}")
            else:
                print(f"No tenes mas pociones")
        if vidaenemigo > 0:
            vidajugador -= ataque_enemigo
            print("¡El enemigo te atacó por 12 puntos de daño!")
if vidajugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print(f"DERROTA. {nombre} has caído en combate.")







