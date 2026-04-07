nombre=input("cliente:  ").strip()

while nombre == "" or not nombre.isalpha():
    print("¡Error!, ingresar un nombre que no sea vacio y que contenga solo letras")
    nombre=input("cliente:  ").strip()

cantidad_str= input("Ingrese la cantidad de productos a comprar: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error!, ingrese un numero entero positivo mayor a cero")
    cantidad_stri= input("Ingrese la cantidad de productos a comprar: ").strip()

cantidad_int= int(cantidad_str)

total_sin_descuento= 0 
total_con_descuento= 0.0

for i in range(1,cantidad_int+1):
    precio_str= input(f" Producto{i} - Precio:  ").strip()
    
    while not precio_str.isdigit() or int(precio_str) ==0:
        print("Error: el precio debe ser entero positivo")
        precio_str= input(f" Producto{i} - Precio:  ").strip()
        
    precio_int= int(precio_str)

    descuento =input("Descuento (S/N)").strip().lower()
    
    while descuento != "s" and descuento != "n":
        print("Error: Ingrese S para si o N para no" )
        descuento =input("Descuento (S/N)").strip().lower()
    
    total_sin_descuento += precio_int

    if descuento == "s":
        precio_final = precio_int * 0.9
    else: 
        precio_final = precio_int

    total_con_descuento += precio_final

ahorro_total= total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_int

print()
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio: ${promedio:.2f}")

