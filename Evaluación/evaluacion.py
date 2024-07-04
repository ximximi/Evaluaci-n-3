import csv

import random

total_pedidos = []
    
def pedido_id():
    
    id = random.randint(99999,999999)
    print (f"{id}")
    return id

def registrar_pedido():
    
    while True:
        nombre = input("Ingrese el nombre: ")
        if not nombre.strip():
            print ("Rellene el campo")
        else: 
            break
    
    while True:
        apellido = input ("Ingrese el apellido: ")
        if not apellido.strip():
            print ("Rellene el campo")
        else: 
            break

    while True:
        direccion = input ("Ingrese la dirección: ")
        if not direccion.strip():
            print ("Rellene el campo")
        else: 
            break

    while True:
        comuna = input("Ingrese la comuna en la que reside: ")
        if not nombre.strip():
            print ("Rellene el campo")
        else: 
            break

    while True:
        try:
            disp_6 = int(input ("Ingrese cuántos dispensadores de 6L quiere: "))
        except ValueError:
            print("Ingrese un número (0 es válido)")
            continue
        try:
            disp_10 = int(input ("Ingrese cuántos dispensadores de 10L quiere: "))
        except ValueError:
            print("Ingrese un número (0 es válido)")
            continue
        try:
            disp_20 = int(input ("Ingrese cuántos dispensadores de 20L quiere: "))
        except ValueError:
            print("Ingrese un número (0 es válido)")
            continue

        total_cil = disp_6 + disp_10 + disp_20
        if total_cil > 0:
            break    
        else:
            print ("El pedido debe contener al menos un cilindro")
    #La empresa vende dispensadores de 6, 10 y 20 litros

    pedido = [
        nombre,
        apellido,
        direccion,
        comuna,
        disp_6,
        disp_10,
        disp_20
    ]

    total_pedidos.append(pedido)
    print("Pedido registrado")
    #print (f"Este es el pedido{total_pedidos}")

def listar_pedido():
    
    if not total_pedidos:
        print("Ingrese un pedido primero")
        return

    for pedido in total_pedidos:
        print (f"Este es el pedido: ")
        print ("ID del pedido:\n")
        pedido_id()
        print ("Cliente\tDirección\tSector\tDisp.6lts\tDisp.10lts\t Disp.20lts")
        print (f"{pedido[0]} {pedido[1]}\t{pedido[2]}\t{pedido[3]}\t{pedido[4]}\t{pedido[5]}\t{pedido[6]}")

def imprimir():
    #sectores = ["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]

    with open ("Hoja_de_ruta.csv", "w", newline= "") as file:
        escritor = csv.writer(file)
        escritor.writerow ("Cliente, Dirección, Sector, Disp.6lts, Disp.10lts, Disp.20lts")
        for pedido in total_pedidos:
            print (f"{pedido[0]} {pedido[1]}, {pedido[2]}, {pedido[3]}, {pedido[4]}, {pedido[5]}, {pedido[6]}")




def menu():
    print("------CleanWasser------")
    while True:
        print("-----------------------")
        print("1. Registrar pedido\n2. Listar todos los pedidos\n3. Imprimir hoja de ruta\n4. Buscar un pedido por ID\n5. Salir del programa")
        opc = input("Seleccione una opción: ")
        
        if opc == "1":
            registrar_pedido()
        
        elif opc == "2":
            listar_pedido()
        elif opc == "3":
            imprimir()
        elif opc == "4":
            print ("No hay servicio")

        elif opc == "5":
            print ("Saliendo del programa...")
            break

menu()