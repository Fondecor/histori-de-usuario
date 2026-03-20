# Lista global para almacenar los productos del inventario
inventario = []


def agregar_producto():
    """
    Función para solicitar datos de un producto y almacenarlo en la lista inventario.
    Pide nombre, precio y cantidad, validando que precio y cantidad sean números positivos.
    """
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    # Validación del precio (debe ser un número positivo)
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio > 0:
                break
            else:
                print("Error: El precio debe ser un valor positivo. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un número válido para el precio.")
    
    # Validación de la cantidad (debe ser un número entero positivo)
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad > 0:
                break
            else:
                print("Error: La cantidad debe ser un valor entero positivo. Intente nuevamente.")
        except ValueError:
            print("Error: Ingrese un número entero válido para la cantidad.")
    
    # Crear diccionario del producto y agregarlo al inventario
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente!\n")


def mostrar_inventario():
    """
    Función para recorrer y mostrar todos los productos del inventario.
    Si el inventario está vacío, muestra un mensaje informativo.
    """
    print("\n--- Inventario Actual ---")
    if not inventario:
        print("El inventario se encuentra vacío.\n")
        return
    
    # Recorrer el inventario con bucle for y mostrar cada producto
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
    print("")


def calcular_estadisticas():
    """
    Función para calcular y mostrar estadísticas básicas del inventario:
    - Valor total (suma de precio * cantidad de cada producto)
    - Cantidad total de productos registrados
    """
    print("\n--- Estadísticas del Inventario ---")
    if not inventario:
        print("No se pueden calcular estadísticas porque el inventario está vacío.\n")
        return
    
    valor_total = 0.0
    cantidad_total = 0
    
    # Calcular sumatorias recorriendo el inventario
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        cantidad_total += producto["cantidad"]
    
    print(f"Valor total del inventario: {valor_total:.2f}")
    print(f"Cantidad total de productos registrados: {cantidad_total}\n")


def main():
    """
    Función principal que gestiona el menú y el flujo del programa.
    Usa un bucle while para mantener el programa en ejecución hasta que el usuario elija salir.
    Valida la opción ingresada por el usuario con condicionales if/elif/else.
    """
    print("=== Sistema de Gestión de Inventario ===")
    
    while True:
        # Mostrar menú de opciones
        print("Seleccione una acción:")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        
        # Solicitar y validar la opción del usuario
        opcion = input("Ingrese el número de la opción deseada: ").strip()
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print(f"\nError: Opción '{opcion}' no válida. Por favor, ingrese un número entre 1 y 4.\n")


# Ejecutar la función principal al iniciar el programa
if __name__ == "__main__":
    main()
