import os, time
os.system("cls")

flag = True
pokebola = 0
revivir = 0
pocion = 0
baya = 0

contador_producto = 0
while flag:
    time.sleep(0.2)
    print("\t>>>TIENDA POKEMON<<<")
    time.sleep(0.2)
    print("1. Pokebola $1000")
    time.sleep(0.2)
    print("2. Poción $1500")
    time.sleep(0.2)
    print("3. Revivir $3000")
    time.sleep(0.2)
    print("4. Baya $500")
    time.sleep(0.2)
    print("5. Finalizar compra")
    time.sleep(0.2)
    try:
        opcion = int(input("\t>>>Ingrese una opcion<<<\n"))
        if opcion == 1:
            cantidad = int(input("ingrese cantidad a comprar\n"))
            pokebola = 1000 * cantidad
            print("pokebola ha sido agregada con exito")
            contador_producto = contador_producto + cantidad
        elif opcion == 2:
            cantidad = int(input("ingrese cantidad a comprar\n"))
            pocion = 1500 * cantidad
            contador_producto = contador_producto + cantidad
            print("pocion ha sido agregada con exito")
        elif opcion == 3:
            cantidad = int(input("ingrese cantidad a comprar\n"))
            revivir = 3000  * cantidad
            contador_producto = contador_producto + cantidad
            print("revivir ha sido agregada con exito")
        elif opcion == 4:
            cantidad = int(input("ingrese cantidad a comprar\n"))
            baya = 500 * cantidad
            contador_producto = contador_producto + cantidad
            print("baya ha sido agregada con exito")
        elif opcion == 5:
            flag = False
        else:
            print("Opcion ingresada no existe , intente nuevamente")  
    except:
        print("ingrese valor numerico entero")
        
    

os.system("cls") 
total_compra = pokebola + pocion + revivir + baya   

    


print(f"valor por pokebolas: ${pokebola}")
print(f"valor por pociones: ${pocion}")
print(f"valor por revivir: ${revivir}")
print(f"valor por bayas: ${baya}")
print(f"cantidad de productos a comprar: {contador_producto}") 
print(f"Total a pagar sin dscto: ${total_compra}")
if total_compra >= 5000:
    total_compradesc = total_compra * 0.90
    print(f"Total con descuento por compras sobre $5000 pesos: {total_compradesc}")
else:
    total_compradesc = total_compra
if total_compra >= 10000:
    total_compradesc2 = total_compradesc * 0.95
    print(f"Total con segundo descuento por compras sobre $10000 pesos: {total_compradesc2}")
else:
    total_compradesc2 = total_compradesc


