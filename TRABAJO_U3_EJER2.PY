usuario_correcto= "alumno"
contraseña_correcta= "python123"

intentos= 0 

while intentos < 3:
    usuario= input("Ingrese el usuario:  ").strip()
    contraseña= input("Ingrese la contraseña:  ").strip()
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("acceso concedido")
        break
    else:
        intentos+=1
        print("Los datos ingresados no son correctos")
if intentos == 3:
    print("Cuenta bloqueada!!")

while True:
       print("1. Estado de Incripcion. ") 
       print("2. Cambio de clave.  ")
       print("3. Mostrar mensaje motivacional. ")
       print("4. Salir.")
       
       opcionstr = input("Seleccione una de las opciones dadas:  ").strip()
       if not opcionstr.isdigit() or int(opcionstr) == 0:
            print("Error: Ingrese el numero de opcion valido")
            continue
       opcionint= int(opcionstr)
       if not opcionint in range (1,5):
            print("Error: No es un numero valido de opciones")
            continue
       if opcionint == 1:
            print("Estado: Inscripto")
       elif opcionint == 2:
            nueva_contraseña = input("Ingrese nueva contraseña: ").strip()
            if len(nueva_contraseña) < 6:
                print("Error: la contraseña debe tener como minimo 6 digitos")
                continue

            confirmar_contraseña = input("Confirme la nueva contraseña: ").strip()
            if nueva_contraseña == confirmar_contraseña:
                contraseña_correcta = nueva_contraseña
                print("Usted actualizo correctamente la contraseña")
            else:
                print("Error: las contraseñas no coinciden")
       elif opcionint == 3:
            print("Segui asi, vos podes!!!")

       elif opcionint == 4:
            print("Usted esta saliendo del sistema!!")
            break


            
            
         
