# histori-de-usuario
Inventario.py - Programa de Gestión Básica de Productos
 
 
 
Descripción
 
Este script en Python permite al usuario ingresar información de un producto (nombre, precio unitario y cantidad), valida que los datos numéricos sean positivos y de tipo correcto, calcula el costo total y muestra un resumen de la información.
 
 
 
Características
 
- Solicita el nombre del producto como texto.
- Valida que el precio sea un número flotante positivo.
- Valida que la cantidad sea un número entero positivo.
- Calcula el costo total como el producto de precio y cantidad.
- Muestra un resumen claro de los datos ingresados y el total calculado.
 
 
 
Cómo Usar
 
1. Asegúrate de tener Python instalado en tu sistema (versión 3.x recomendada).
2. Descarga el archivo  inventario.py .
3. Abre una terminal o consola y navega hasta el directorio donde se encuentra el archivo.
4. Ejecuta el script con el comando:
bash
  
python inventario.py
 
5. Sigue las instrucciones en pantalla para ingresar los datos del producto:
- Ingresa el nombre del producto cuando se solicite.
- Ingresa el precio unitario (debe ser un número positivo; si ingresas texto o un valor negativo, se pedirá nuevamente).
- Ingresa la cantidad (debe ser un número entero positivo; se validará igual que el precio).
6. Una vez ingresados los datos válidos, se mostrará el resumen con el costo total.
 
 
 
Ejemplo de Ejecución
 
plaintext
  
Ingrese el nombre del producto: Laptop
Ingrese el precio unitario del producto: 899.99
Ingrese la cantidad del producto: 3
Producto: Laptop | Precio: 899.99 | Cantidad: 3 | Total: 2699.97
 
 
 
 
Estructura del Código
 
- Entrada de datos: Se solicitan los valores al usuario con validaciones para asegurar su corrección.
- Operación matemática: Se calcula el costo total multiplicando precio y cantidad.
- Salida de resultados: Se muestra un resumen formateado en la consola.
 
 
 
Licencia
 
Este proyecto es de uso libre, puedes modificarlo y distribuirlo según tus necesidades.
