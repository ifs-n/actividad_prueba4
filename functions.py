
productos = [{
    "nombre":"Pao de queijo", "stock":5, "precio":1000, "disponible": False
}]

def verificar_largo(string):
    verificar = True
    while verificar:
        if len(string) <= 0 or string.startswith(" ") == True:
            return False
        else:
            return True

def verificar_entero(numero):
    if isinstance(numero, int) and numero > 0:
        return True
    else:
        return False

def verificar_flotante(numero):
    if isinstance(numero, float) and numero > 0:
        return True
    else:
        return False

def verificar_estado(x):
    if x["estado"] == True:
        return "En stock"
    else:
        return "Sin stock"
    
def imprimir_menu():
    print("==== Menú Principal ===\n")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir\n")
    print("=======================")

def selector_opciones():
    try:
        invalida = "Opción inválida"
        opcion_selector = int(input("Ingrese una opción: \n"))
        if opcion_selector >= 1 and opcion_selector <= 6:
            return opcion_selector
        else:
            return invalida
    except:
        return "La opción ingresada no es un número entero válido."

def agregar_producto():
    print("== REGISTRAR PRODUCTO ==")
    
    nombre = input("Ingrese el nombre del producto: \n").title()
    while verificar_largo(nombre) == False:
        nombre = input("El nombre del producto no puede quedar vacío.\nIngrese el nombre nuevamente:\n").title()
    
    stock = int(input("Ingrese el stock:\n"))
    while verificar_entero(stock) == False:
        stock = int(input("El stock debe ser un número entero mayor a cero:\n"))

    precio = float(input("Ingrese el precio del producto:\n"))
    while verificar_flotante(precio) == False:
        precio = float("El precio debe ser un número mayor a cero: \n")
    
    producto = {
        "nombre":nombre,
        "stock":stock,
        "precio":precio,
        "disponible":False
    }
    productos.append(producto)

def buscar_producto():
    print("== BUSCAR PRODUCTO ==")
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        buscar = input("Ingrese el nombre del producto a buscar: \n").title()
        while verificar_largo(buscar) == False:
            buscar = input("El campo de búsqueda no puede estar vacío: \n").title()
        encontrado = False
        for p in productos:
            if p["nombre"] == buscar:
                encontrado = True
                print("== Producto encontrado ==")
                print(f"Nombre: {p["nombre"]}")
                print(f"Especie: {p["stock"]}")
                print(f"Edad: ${p["precio"]}")
                print(f"Estado: {verificar_estado(p)}")
        if encontrado == False:
                print("El producto buscado no esta registrado.")

def eliminar_producto():
    print("== ELIMINAR REGISTRO DE MASCOTA ==")
    if len(mascotas) == 0:
        print("No hay mascotas registradas")
    else:
        eliminar = input("Ingrese el nombre de la mascota que desea eliminar:\n").title()
        while verificar_largo(eliminar) == False:
            eliminar = input("El campo de busqueda para eliminar no puede estar vacío: \n")
        eliminado = False
        for m in mascotas:
            if m["nombre"] == eliminar:
                mascotas.remove(m)
                print(f"El registro de la mascota de nombre {eliminar} ha sido borrado 💀")
                eliminado = True
        if eliminado == False:
            print("No existe una mascota registrada con el nombre ingresado.")

def actualizar_estados():
    print("== ACTUALIZAR ESTADOS ==")
    if len(mascotas) == 0:
        print("No hay mascotas registradas.")
    else:
        actualizados = 0
        for m in mascotas:
            verificado = False
            if m["estado"] == False:
                if m["peso"] > 2 and m["edad"] < 15:
                    m["estado"] = True
                    verificado = True
                    actualizados += 1
            if verificado == False:
                m["estado"] = False
                actualizados += 1
        print(f"{actualizados} Estados Actualizados")


def mostrar_mascotas():
    actualizar_estados()
    print("== MOSTRAR MASCOTAS ==")
    if len(mascotas) == 0:
        print("No hay mascotas registradas.")
    else:
        for m in mascotas:
            print(f"*** Mascota N°{mascotas.index(m) + 1} ***")
            print(f"Nombre: {m["nombre"]}")
            print(f"Especie: {m["especie"]}")
            print(f"Edad: {m["edad"]}")
            print(f"Peso: {m["estado"]}")
            print(f"Estado: {verificar_estado(m)}")
            print("*************************")