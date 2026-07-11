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

# MENÚ PRINCIPAL
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
    total_unidades = 0
    for i in productos:
        if productos[i][1].lower() == categoria.lower():
            total_unidades += stock[i][1]
    print(f"El total de unidades disponibles es: {total_unidades}")


def busqueda_precio(p_min, p_max):
    lista_productos_precio = []
    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
        for i in stock:
            if p_min <= stock[i][0] <= p_max and stock[i][1] != 0:
                lista_productos_precio.append(f"{productos[i][0]}-{i}")
        if lista_productos_precio != []:
            lista_productos_precio.sort()
            print(f"Los productos encontrados son: {lista_productos_precio}")
        else:
            print("No hay productos en ese rango de precios.")
    else:
        print("Rango de precios inválido.")


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper()
    for i in stock:
        if codigo == i:
            stock[i][0] = nuevo_precio
            return True
    return False


def validacion_codigo(codigo):
    codigo = codigo.upper()
    for i in productos:
        if codigo == i:
            return True
    return False


def vacio_espacios_en_blanco(string):
    if string.split():
        return True
    return False


def validacion_peso(peso):
    if peso > 0:
        return True
    return False


def validacion_sn(valor):
    return valor.lower() in ["s", "n"]


def validacion_precio(precio):
    if precio > 0:
        return True
    return False


def validacion_unidades(unidades):
    if unidades >= 0:
        return True
    return False


def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    codigo = codigo.upper()
    if codigo in productos:
        return False
    productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
    stock[codigo] = [precio, unidades]
    return True


def eliminar_producto(codigo):
    codigo = codigo.upper()
    if codigo not in productos:
        return False
    del productos[codigo]
    del stock[codigo]
    return True


while True:
    try:
        mostrar_menu()
        opcion = int(input("Ingrese opción: "))
        if opcion == 1:
            categoria = input("Ingrese categoría a consultar: ")
            unidades_categoria(categoria)
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    busqueda_precio(p_min, p_max)
                    break
                except:
                    print("Debe ingresar valores enteros")
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código del producto: ")
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if actualizar_precio(codigo, nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                actualizar = input("¿Desea actualizar otro precio (s/n)?: ")
                if actualizar.lower() == "n":
                    break
        elif opcion == 4:
            codigo = input("Ingrese código del producto: ")
            nombre = input("Ingrese nombre: ")
            categoria = input("Ingrese categoría: ")
            marca = input("Ingrese marca: ")
            peso_kg = float(input("Ingrese peso (kg): "))
            importado = input("¿Es importado? (s/n): ").lower()
            cachorro = input("¿Es para cachorro? (s/n): ").lower()
            precio = int(input("Ingrese precio: "))
            unidades = int(input("Ingrese unidades: "))

            if not vacio_espacios_en_blanco(codigo):
                print("Código inválido")
            elif validacion_codigo(codigo):
                print("El código ya existe")
            elif not vacio_espacios_en_blanco(nombre):
                print("Nombre inválido")
            elif not vacio_espacios_en_blanco(categoria):
                print("Categoría inválida")
            elif not vacio_espacios_en_blanco(marca):
                print("Marca inválida")
            elif not validacion_peso(peso_kg):
                print("Peso inválido")
            elif not validacion_sn(importado):
                print("Debe ingresar s o n")
            elif not validacion_sn(cachorro):
                print("Debe ingresar s o n")
            elif not validacion_precio(precio):
                print("Precio inválido")
            elif not validacion_unidades(unidades):
                print("Cantidad de unidades inválida")
            else:
                es_importado = importado == "s"
                es_para_cachorro = cachorro == "s"
                if agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
                    print("Producto agregado")
                else:
                    print("El código ya existe")
        elif opcion == 5:
            codigo = input("Ingrese código: ")
            if eliminar_producto(codigo):
                print("Producto eliminado")
            else:
                print("El código no existe")
        elif opcion == 6:
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida")
    except:
        print("Debe seleccionar una opción válida")