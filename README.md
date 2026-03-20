Sistema de Gestión de Inventario 📦
 
Sistema básico desarrollado en Python para administrar un inventario de productos, con funcionalidades para agregar elementos, visualizar la información y calcular estadísticas. Cuenta con validaciones de entrada de datos y una estructura modularizada y documentada.
 
🚀 Características
 
- Agregar productos: Registra nuevos elementos con nombre, precio y cantidad, validando que los valores numéricos sean positivos y correctos.
- Mostrar inventario: Visualiza todos los productos almacenados de forma clara y ordenada.
- Calcular estadísticas: Obtiene el valor total del inventario y la cantidad total de unidades registradas.
- Manejo de errores: Gestiona entradas inválidas y muestra mensajes informativos para guiar al usuario.
- Interfaz intuitiva: Menú interactivo que facilita la navegación por las funcionalidades del sistema.
 
📋 Requisitos
 
- Python 3.x (versión recomendada: 3.8 o superior)
- No requiere librerías externas, funciona con módulos integrados en el lenguaje.
 
🛠️ Uso
 
1. Clona el repositorio o descarga el archivo del código:
bash
  
git clone https://github.com/tu-usuario/sistema-gestion-inventario.git
cd sistema-gestion-inventario
 
2. Ejecuta el programa desde la terminal o consola:
bash
  
python inventario.py
 
3. Sigue las instrucciones del menú interactivo:
- Selecciona la opción  1  para agregar nuevos productos.
- Selecciona la opción  2  para ver el inventario completo.
- Selecciona la opción  3  para consultar las estadísticas del inventario.
- Selecciona la opción  4  para salir del sistema.
 
Ejemplo de funcionamiento
 
plaintext
  
=== Sistema de Gestión de Inventario ===
Seleccione una acción:
1. Agregar producto
2. Mostrar inventario
3. Calcular estadísticas
4. Salir
Ingrese el número de la opción deseada: 1

--- Agregar Nuevo Producto ---
Ingrese el nombre del producto: Laptop
Ingrese el precio del producto: 899.99
Ingrese la cantidad del producto: 5
Producto 'Laptop' agregado exitosamente!

Seleccione una acción:
...
 
 
📂 Estructura del código
 
Elemento Descripción 
 inventario  Lista global que almacena cada producto como un diccionario con sus datos. 
 agregar_producto()  Función que solicita y valida los datos de un producto para agregarlo al inventario. 
 mostrar_inventario()  Función que recorre la lista y muestra todos los productos registrados. 
 calcular_estadisticas()  Calcula y muestra el valor total del inventario y la cantidad total de unidades. 
 main()  Función principal que gestiona el menú y el flujo de ejecución del programa. 
 
El código cuenta con documentación interna (docstrings) que explica el propósito y funcionamiento de cada función.
 
📝 Objetivo del proyecto
 
Desarrollar un sistema práctico que integre conceptos fundamentales de Python:
 
- Estructuras de control (condicionales y bucles)
- Almacenamiento de datos con listas y diccionarios
- Modularización del código mediante funciones
- Validación y manejo de entradas de usuario
- Documentación clara del código
 
🤝 Contribuciones
 
Las contribuciones son bienvenidas. Si deseas mejorar el sistema, agregar funcionalidades o corregir errores, por favor abre un issue o envía un pull request con tus cambios.
 
📄 Licencia
 
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo  LICENSE  para más detalles.
 
¿Te gustaría que agregue una sección de funcionalidades futuras o ejemplos de posibles mejoras al README?
