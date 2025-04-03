def hacer_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar clientes")
    print("4. Nuevo menu")
    print("0. Salir del sistema")
    print("Seleccione una opción...")
    opcion = int(input())
    return opcion

def registrar_cliente():
    nombre_cliente = input("Digite el nombre: ")
    apellido_cliente = input("Digite el apellido: ")
    cedula_cliente = input("Digite la cédula: ")
    info_cliente = [nombre_cliente, apellido_cliente, cedula_cliente]
    return info_cliente

def guardar_cliente(info_cliente, bd_cliente):
    bd_cliente.append(info_cliente)
    return bd_cliente

def eliminar_cliente(bd_cliente):
    cedula = input("Ingrese la cédula del cliente a eliminar: ")
    for cliente in bd_cliente:
        if cliente[2] == cedula:
            bd_cliente.remove(cliente)
            print("Cliente eliminado exitosamente.")
            return
    print("Cliente no encontrado.")

def mostrar_clientes(bd_cliente):
    print("\n  Lista de Clientes ")
    if not bd_cliente:
        print("No hay clientes registrados.")
    else:
        for cliente in bd_cliente:
            print(f"{cliente[0]} {cliente[1]} - Cédula: {cliente[2]}")

def nuevo_menu(bd_cliente):
    print("\n 3 Nuevo Menú ")
    print("1. Combinar datos")
    print("2. Ordenar")
    print("3. Invertir la secuencia")
    print("0. Volver al menú principal")
    opcion = int(input("Seleccione una opción: "))
    
    match opcion:
        case 1:
            nombres = [cliente[0] for cliente in bd_cliente]  # Extraemos los nombres
            apellidos = [cliente[1] for cliente in bd_cliente]  # Extraemos los apellidos
            combinados = zip(nombres, apellidos)

            print("\n- Combinación de Datos -")
            for nombre, apellido in combinados:
                print(f"Nombre Completo: {nombre} {apellido}")
            print("Funcionalidad de combinar datos completada.")
        case 2:
            # Ordenar los clientes por nombre
            bd_cliente.sort(key=lambda x: x[0])  # Ordenar por nombre
            print("\n--- Clientes Ordenados ---")
            mostrar_clientes(bd_cliente)
        
        case 3:
            # Invertir el orden de la lista de clientes
            bd_cliente.reverse()
            print("\n--- Secuencia Invertida ---")
            mostrar_clientes(bd_cliente)
        
        case 0:
            print("Volviendo al menú principal...")
        
        case _:
            print("Opción no válida. Intente nuevamente.")

# Base de datos de clientes
bd_cliente = []


while True:
    opcion = hacer_menu()
    
    match opcion:
        case 1:
            cliente = registrar_cliente()
            guardar_cliente(cliente, bd_cliente)
            print("Cliente registrado exitosamente.")
        
        case 2:
            eliminar_cliente(bd_cliente)
        
        case 3:
            mostrar_clientes(bd_cliente)
        
        case 4:
            nuevo_menu(bd_cliente)
        
        case 0:
            print("Saliendo del sistema...")
            break
        
        case _:
            print("Opción no válida. Intente de nuevo.")

print("Programa finalizado.")
