# Restaurante App - Semana 15

## Descripción

Proyecto correspondiente a la Semana 15 de la asignatura
Programación Orientada a Objetos.

Esta actividad continúa la evolución de Restaurante App
desarrollada durante las semanas anteriores.

En la Semana 15 se estudian los conceptos fundamentales de
manejo de eventos en interfaces gráficas mediante Tkinter.

La aplicación incorpora una sección de ventas para observar
el flujo completo desde la interacción del usuario hasta la
persistencia y la respuesta visual.

## Objetivo de Semana 15

Comprender el flujo:

Usuario -> Componente -> Evento -> Callback ->
Servicio -> Modelo/Datos -> Respuesta visual

La sección Ventas permite relacionar un usuario registrado
con un producto registrado y la fecha de la operación.

## Estructura

restaurante_app/
├── assets/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── login_view.py
│   └── main_view.py
└── main.py

## Funcionalidades

### Login

Permite ingresar al sistema mediante usuario y contraseña.

### Productos

Permite:

- Registrar productos.
- Consultar productos.
- Actualizar productos.
- Eliminar productos.
- Visualizar los productos mediante Treeview.

### Usuarios

Permite consultar los usuarios registrados.

### Ventas

La sección Ventas incorpora:

- ttk.Combobox para seleccionar un usuario.
- ttk.Combobox para seleccionar un producto.
- ttk.Button para solicitar el registro.
- ttk.Treeview para presentar las ventas.
- messagebox para comunicar el resultado.

Cada venta contiene:

- Identificador.
- Usuario.
- Producto.
- Fecha.

Los identificadores se generan automáticamente con el
formato V001, V002, V003, etc.

## Manejo de eventos

El botón Registrar venta utiliza command= para asociarse
con el callback registrar_venta.

El flujo utilizado es:

1. El usuario selecciona un usuario.
2. El usuario selecciona un producto.
3. Presiona Registrar venta.
4. Tkinter ejecuta el callback registrar_venta.
5. El callback obtiene los valores seleccionados.
6. MainView solicita la operación a RestauranteServicio.
7. RestauranteServicio valida los datos.
8. Se crea un objeto Venta.
9. La venta se guarda en ventas.json.
10. MainView refresca el Treeview.
11. Se presenta un mensaje de confirmación.

La interfaz no escribe directamente los archivos JSON.

## Persistencia

ArchivoServicio se encarga de leer y escribir los archivos JSON.

Los datos utilizados son:

- datos/productos.json
- datos/usuarios.json
- datos/ventas.json

Las ventas permanecen almacenadas después de cerrar y volver
a ejecutar la aplicación.

## Credenciales de prueba

Usuario: admin
Contraseña: 1234

Usuario: empleado
Contraseña: abcd

## Ejecución

Ubicarse dentro de la carpeta restaurante_app y ejecutar:

python main.py