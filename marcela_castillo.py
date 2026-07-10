
lista_productos=[]
lista_stock=[]


productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False]
} 

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3]
}

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

def unidades_categoria(categoria):
     total=0
     #print(f"Unidades disponibles en la categoría '{categoria}':")
     for i in productos:
        if productos[i][1] == categoria:
            print(f"Producto: {productos[i][0]}, Unidades: {stock[i][1]}")
            if stock[i][1] > 0:
                lista_productos.append(productos[i][0].lower())
                lista_stock.append(stock[i][1])

def busqueda_precio(p_min, p_max):
    print(f"Productos con precio entre {p_min} y {p_max}:")
    for codigo, datos in productos.items():
        precio = stock[codigo][0]
        if p_min <= precio <= p_max:
            print(f"Producto: {datos[0]}, Precio: {precio}")

def actualizar_precio(codigo, nuevo_precio):
    for i in stock:
        if codigo == i:
            stock[i][0] = nuevo_precio
            print("Precio actualizado")
            return True
    return False

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    if codigo in productos:
        print("El código del producto ya existe. No se puede agregar.")
        return False
    else:
        productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
        stock[codigo] = [precio, unidades]
        print("Producto agregado correctamente.")
        return True

def eliminar_producto(codigo):
    if codigo in productos:
        del productos[codigo]
        del stock[codigo]
        print("Producto eliminado correctamente.")
        return True
    else:
        print("El código del producto no existe. No se puede eliminar.")
        return False
def validacion_codigo(codigo):
    for i in productos :
        if codigo == i:
            return True        
    return False

def validacion_categoria(categoria):
    if categoria in ["comida", "higiene", "snack", "accesorio"]:
        return True
    return False
            

def vacio_espacios_en_blanco (string):
    if string.split():
        return True
    return False

def validacion_peso_kg(peso_kg):
    if peso_kg > 0:
        return True
    return False
def validacion_es_importado(es_importado):
    if es_importado.lower() in ['s', 'n']:
        return True
    return False
def validacion_es_para_cachorro(es_para_cachorro):
    if es_para_cachorro.lower() in ['s', 'n']:
        return True
    return False


while True:
    try:
        mostrar_menu()
        opcion = int(input("Seleccione una opción (1-6): "))

        if opcion == 1:
            unidades_por_categoria = ()
            categoria = input("Ingrese la categoría: ").lower()
            unidades_categoria(categoria)
            if categoria=="comida" or categoria=="higiene" or categoria=="snack" or categoria=="accesorio":
                print(f"Unidades disponibles en la categoría '{categoria}':")
            else:
                print("Categoría inválida. Por favor, ingrese una categoría válida.")
            for i in productos:
                if productos[i][1] == categoria:
                    print(f"Producto: {productos[i][0]}, Unidades: {stock[i][1]}")


        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    busqueda_precio(p_min,p_max)
                    break
                except:
                    print("No hay productos en ese rango de precios.")
     # Lógica para búsqueda de productos por rango de precio
          
     
        elif opcion == 3:
            while True:
                try:
                    codigo = input("Ingrese el código del producto a actualizar: ")
                    if codigo not in productos:
                        print("No existe el código del producto")
                        
                except ValueError:
                    print("Por favor, ingrese un código válido.")
                else:
                        precio_nuevo = int(input("Ingrese nuevo precio del producto: "))
                        actualizar_precio(codigo, precio_nuevo)
                        if actualizar_precio(codigo,precio_nuevo):
                            print("Precio actualizado correctamente.")
                            break
                        else:
                            actualizar = input("¿Desea actualizar otro precio (s/n)?: ")
                            if actualizar.lower() == "n":
                                break
        elif opcion == 4:
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            marca = input("Ingrese la marca del producto: ")
            peso_kg = float(input("Ingrese el peso en kg del producto: "))
            es_importado = input("¿El producto es importado? (s/n): ").lower() == 's'
            es_para_cachorro = input("¿El producto es para cachorro? (s/n): ").lower() == 's'
            precio = int(input("Ingrese el precio del producto: "))
            unidades = int(input("Ingrese la cantidad de unidades disponibles: "))
            agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades)

            if not validacion_codigo(codigo):
                print("Error: El código del producto ya existe.")
            elif validacion_codigo(codigo) and not vacio_espacios_en_blanco(nombre):
                print("Error: El nombre del producto no puede estar vacío.")
            elif validacion_codigo(codigo) and vacio_espacios_en_blanco(nombre):
                print("Producto agregado correctamente.")
            elif not vacio_espacios_en_blanco(nombre):
                print("Error: El nombre del producto no puede estar vacío.")
            elif not validacion_peso_kg(peso_kg):
                print("Error: El peso del producto debe ser mayor a 0.")
            elif not validacion_es_importado(es_importado):
                print("Error: La opción de importado debe ser 's' o 'n'.")
            elif not validacion_es_para_cachorro(es_para_cachorro):
                print("Error: La opción de para cachorro debe ser 's' o 'n'.")
            
        elif opcion == 5:
            codigo = input("Ingrese el código del producto a eliminar: ")
            eliminar_producto(codigo)               

     
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")