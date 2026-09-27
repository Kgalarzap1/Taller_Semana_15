from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox


class MainView(tk.Frame):

    def __init__(
        self,
        master,
        restaurante_servicio,
        usuario_actual,
        al_cerrar_sesion
    ) -> None:

        super().__init__(master, bg="#f5f5f5")

        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion

        self.frame_contenido = None

        # =================================================
        # VARIABLES DE PRODUCTOS
        # =================================================

        self.producto_codigo_entry = None
        self.producto_nombre_entry = None
        self.producto_categoria_entry = None
        self.producto_precio_entry = None
        self.producto_stock_entry = None
        self.tabla_productos = None

        # =================================================
        # VARIABLES DE USUARIOS
        # =================================================

        self.tabla_usuarios = None

        # =================================================
        # VARIABLES DE VENTAS
        # =================================================

        self.usuario_venta_combo = None
        self.producto_venta_combo = None
        self.tabla_ventas = None

        self.opciones_usuarios_venta = {}
        self.opciones_productos_venta = {}

        # =================================================
        # RUTAS DE ASSETS
        # =================================================

        self.ruta_assets = (
            Path(__file__).resolve().parent.parent / "assets"
        )

        self.ruta_iconos = self.ruta_assets / "icons"
        self.ruta_logo = self.ruta_assets / "logo"

        # =================================================
        # CARGAR ICONOS
        # =================================================

        self.iconos = {}

        nombres_iconos = (
            "home",
            "books",
            "users",
            "sales",
            "logout",
            "add",
            "search",
            "edit",
            "delete",
            "clean"
        )

        for nombre in nombres_iconos:

            self.iconos[nombre] = tk.PhotoImage(
                file=str(
                    self.ruta_iconos / f"{nombre}.png"
                )
            )

        # =================================================
        # CARGAR LOGO
        # =================================================

        self.logo = tk.PhotoImage(
            file=str(
                self.ruta_logo / "logo.png"
            )
        )

        self.logo_sidebar = self.logo.subsample(8, 8)

        # =================================================
        # CONSTRUIR INTERFAZ
        # =================================================

        self.construir_interfaz()

    # =====================================================
    # ESTILO DE BOTÓN OSCURO
    # =====================================================

    def crear_boton_oscuro(
        self,
        contenedor,
        texto,
        icono,
        comando,
        ancho=None
    ):

        boton = tk.Button(
            contenedor,
            text=f"  {texto}",
            image=self.iconos[icono],
            compound="left",
            command=comando,
            bg="#37474F",
            fg="white",
            activebackground="#455A64",
            activeforeground="white",
            relief="flat",
            bd=0,
            font=("Arial", 10),
            cursor="hand2",
            padx=12,
            pady=9,
            anchor="center"
        )

        if ancho is not None:
            boton.configure(width=ancho)

        return boton

    # =====================================================
    # ESTRUCTURA GENERAL
    # =====================================================

    def construir_interfaz(self) -> None:

        # =================================================
        # MENÚ LATERAL
        # =================================================

        frame_sidebar = tk.Frame(
            self,
            bg="#263238",
            width=190,
            padx=16,
            pady=18
        )

        frame_sidebar.pack(
            side="left",
            fill="y"
        )

        frame_sidebar.pack_propagate(False)

        # =================================================
        # LOGO
        # =================================================

        tk.Label(
            frame_sidebar,
            image=self.logo_sidebar,
            bg="#263238"
        ).pack(
            pady=(0, 15)
        )

        # =================================================
        # USUARIO ACTUAL
        # =================================================

        tk.Label(
            frame_sidebar,
            text=(
                "Usuario:\n"
                f"{self.usuario_actual.nombre}"
            ),
            bg="#263238",
            fg="white",
            font=("Arial", 10),
            justify="left"
        ).pack(
            anchor="w",
            pady=(0, 25)
        )

        # =================================================
        # BOTONES DEL MENÚ
        # =================================================

        self.crear_boton_oscuro(
            frame_sidebar,
            "Inicio",
            "home",
            self.mostrar_inicio
        ).pack(
            fill="x",
            pady=4
        )

        self.crear_boton_oscuro(
            frame_sidebar,
            "Productos",
            "books",
            self.mostrar_productos
        ).pack(
            fill="x",
            pady=4
        )

        self.crear_boton_oscuro(
            frame_sidebar,
            "Usuarios",
            "users",
            self.mostrar_usuarios
        ).pack(
            fill="x",
            pady=4
        )

        self.crear_boton_oscuro(
            frame_sidebar,
            "Ventas",
            "sales",
            self.mostrar_ventas
        ).pack(
            fill="x",
            pady=4
        )

        # =================================================
        # SEPARADOR
        # =================================================

        tk.Frame(
            frame_sidebar,
            bg="#90A4AE",
            height=1
        ).pack(
            fill="x",
            pady=15
        )

        # =================================================
        # CERRAR SESIÓN
        # =================================================

        self.crear_boton_oscuro(
            frame_sidebar,
            "Cerrar sesión",
            "logout",
            self.cerrar_sesion
        ).pack(
            fill="x",
            pady=4
        )

        # =================================================
        # CONTENIDO PRINCIPAL
        # =================================================

        self.frame_contenido = tk.Frame(
            self,
            bg="#f5f5f5",
            padx=25,
            pady=20
        )

        self.frame_contenido.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.mostrar_inicio()

    # =====================================================
    # LIMPIAR CONTENIDO
    # =====================================================

    def limpiar_contenido(self) -> None:

        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    # =====================================================
    # INICIO
    # =====================================================

    def mostrar_inicio(self) -> None:

        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="Panel principal",
            bg="#f5f5f5",
            font=("Arial", 22, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            self.frame_contenido,
            text="Resumen general del sistema",
            bg="#f5f5f5",
            font=("Arial", 11)
        ).pack(
            anchor="w",
            pady=(5, 25)
        )

        resumen = tk.LabelFrame(
            self.frame_contenido,
            text="Resumen",
            bg="#f5f5f5",
            padx=20,
            pady=20
        )

        resumen.pack(
            fill="x"
        )

        tk.Label(
            resumen,
            text=(
                "Productos registrados: "
                f"{self.restaurante_servicio.cantidad_productos()}"
            ),
            bg="#f5f5f5",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            pady=5
        )

        tk.Label(
            resumen,
            text=(
                "Usuarios registrados: "
                f"{self.restaurante_servicio.cantidad_usuarios()}"
            ),
            bg="#f5f5f5",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            pady=5
        )

        tk.Label(
            resumen,
            text=(
                "Ventas registradas: "
                f"{self.restaurante_servicio.cantidad_ventas()}"
            ),
            bg="#f5f5f5",
            font=("Arial", 12)
        ).pack(
            anchor="w",
            pady=5
        )

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def mostrar_productos(self) -> None:

        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="Gestión de productos",
            bg="#f5f5f5",
            font=("Arial", 21, "bold")
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        # =================================================
        # FORMULARIO
        # =================================================

        formulario = tk.LabelFrame(
            self.frame_contenido,
            text="Datos del producto",
            bg="#f5f5f5",
            padx=15,
            pady=12
        )

        formulario.pack(
            fill="x",
            pady=(0, 12)
        )

        formulario.columnconfigure(
            1,
            weight=1
        )

        campos = (
            ("Código", 0),
            ("Nombre", 1),
            ("Categoría", 2),
            ("Precio", 3),
            ("Stock", 4)
        )

        entradas = []

        for texto, fila in campos:

            tk.Label(
                formulario,
                text=texto,
                bg="#f5f5f5"
            ).grid(
                row=fila,
                column=0,
                sticky="w",
                padx=5,
                pady=5
            )

            entrada = tk.Entry(
                formulario
            )

            entrada.grid(
                row=fila,
                column=1,
                sticky="ew",
                padx=5,
                pady=5
            )

            entradas.append(entrada)

        (
            self.producto_codigo_entry,
            self.producto_nombre_entry,
            self.producto_categoria_entry,
            self.producto_precio_entry,
            self.producto_stock_entry
        ) = entradas

        # =================================================
        # BOTONES CRUD
        # =================================================

        acciones = tk.Frame(
            formulario,
            bg="#f5f5f5"
        )

        acciones.grid(
            row=5,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(12, 0)
        )

        botones = (
            (
                "Registrar",
                "add",
                self.registrar_producto
            ),
            (
                "Cargar / Consultar",
                "search",
                self.cargar_producto_en_formulario
            ),
            (
                "Actualizar",
                "edit",
                self.actualizar_producto
            ),
            (
                "Eliminar",
                "delete",
                self.eliminar_producto
            ),
            (
                "Limpiar",
                "clean",
                self.limpiar_formulario_producto
            )
        )

        for texto, icono, comando in botones:

            self.crear_boton_oscuro(
                acciones,
                texto,
                icono,
                comando
            ).pack(
                side="left",
                padx=(0, 8)
            )

        # =================================================
        # TABLA DE PRODUCTOS
        # =================================================

        contenedor_tabla = tk.LabelFrame(
            self.frame_contenido,
            text="Productos registrados",
            padx=10,
            pady=10
        )

        contenedor_tabla.pack(
            fill="both",
            expand=True,
            pady=(8, 0)
        )

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock"
        )

        self.tabla_productos = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "codigo": "Código",
            "nombre": "Nombre",
            "categoria": "Categoría",
            "precio": "Precio",
            "stock": "Stock"
        }

        for columna in columnas:

            self.tabla_productos.heading(
                columna,
                text=encabezados[columna]
            )

        self.tabla_productos.column(
            "codigo",
            width=80,
            anchor="center"
        )

        self.tabla_productos.column(
            "nombre",
            width=180
        )

        self.tabla_productos.column(
            "categoria",
            width=140
        )

        self.tabla_productos.column(
            "precio",
            width=90,
            anchor="center"
        )

        self.tabla_productos.column(
            "stock",
            width=80,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            contenedor_tabla,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        self.tabla_productos.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tabla_productos.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.refrescar_productos()

    # =====================================================
    # OBTENER DATOS DE PRODUCTO
    # =====================================================

    def obtener_datos_producto(self):

        return (
            self.producto_codigo_entry.get().strip(),
            self.producto_nombre_entry.get().strip(),
            self.producto_categoria_entry.get().strip(),
            self.producto_precio_entry.get().strip(),
            self.producto_stock_entry.get().strip()
        )

    # =====================================================
    # REGISTRAR PRODUCTO
    # =====================================================

    def registrar_producto(self) -> None:

        try:

            self.restaurante_servicio.registrar_producto(
                *self.obtener_datos_producto()
            )

            self.refrescar_productos()
            self.limpiar_formulario_producto()

            messagebox.showinfo(
                "Productos",
                "Producto registrado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Productos",
                str(error)
            )

    # =====================================================
    # CONSULTAR PRODUCTO
    # =====================================================

    def cargar_producto_en_formulario(self) -> None:

        try:

            codigo = (
                self.producto_codigo_entry
                .get()
                .strip()
            )

            producto = (
                self.restaurante_servicio
                .buscar_producto_por_codigo(
                    codigo
                )
            )

            if producto is None:

                raise ValueError(
                    "No existe un producto con ese código."
                )

            self.limpiar_formulario_producto()

            self.producto_codigo_entry.insert(
                0,
                producto.codigo
            )

            self.producto_nombre_entry.insert(
                0,
                producto.nombre
            )

            self.producto_categoria_entry.insert(
                0,
                producto.categoria
            )

            self.producto_precio_entry.insert(
                0,
                str(producto.precio)
            )

            self.producto_stock_entry.insert(
                0,
                str(producto.stock)
            )

        except ValueError as error:

            messagebox.showerror(
                "Productos",
                str(error)
            )

    # =====================================================
    # ACTUALIZAR PRODUCTO
    # =====================================================

    def actualizar_producto(self) -> None:

        try:

            self.restaurante_servicio.actualizar_producto(
                *self.obtener_datos_producto()
            )

            self.refrescar_productos()
            self.limpiar_formulario_producto()

            messagebox.showinfo(
                "Productos",
                "Producto actualizado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Productos",
                str(error)
            )

    # =====================================================
    # ELIMINAR PRODUCTO
    # =====================================================

    def eliminar_producto(self) -> None:

        try:

            codigo = (
                self.producto_codigo_entry
                .get()
                .strip()
            )

            producto = (
                self.restaurante_servicio
                .buscar_producto_por_codigo(
                    codigo
                )
            )

            if producto is None:

                raise ValueError(
                    "No existe un producto con ese código."
                )

            confirmar = messagebox.askyesno(
                "Productos",
                (
                    "¿Desea eliminar el producto "
                    f"{producto.nombre}?"
                )
            )

            if not confirmar:
                return

            self.restaurante_servicio.eliminar_producto(
                codigo
            )

            self.refrescar_productos()
            self.limpiar_formulario_producto()

            messagebox.showinfo(
                "Productos",
                "Producto eliminado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Productos",
                str(error)
            )

    # =====================================================
    # LIMPIAR FORMULARIO PRODUCTO
    # =====================================================

    def limpiar_formulario_producto(self) -> None:

        entradas = (
            self.producto_codigo_entry,
            self.producto_nombre_entry,
            self.producto_categoria_entry,
            self.producto_precio_entry,
            self.producto_stock_entry
        )

        for entrada in entradas:

            entrada.delete(
                0,
                tk.END
            )

        self.producto_codigo_entry.focus()

    # =====================================================
    # REFRESCAR PRODUCTOS
    # =====================================================

    def refrescar_productos(self) -> None:

        for item in (
            self.tabla_productos.get_children()
        ):

            self.tabla_productos.delete(item)

        for producto in (
            self.restaurante_servicio.listar_productos()
        ):

            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock
                )
            )

    # =====================================================
    # USUARIOS
    # =====================================================

    def mostrar_usuarios(self) -> None:

        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="Usuarios registrados",
            bg="#f5f5f5",
            font=("Arial", 21, "bold")
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        contenedor_tabla = tk.LabelFrame(
            self.frame_contenido,
            text="Consulta de usuarios",
            padx=10,
            pady=10
        )

        contenedor_tabla.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "identificacion",
            "nombre",
            "correo",
            "usuario"
        )

        self.tabla_usuarios = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "identificacion": "Identificación",
            "nombre": "Nombre",
            "correo": "Correo",
            "usuario": "Usuario"
        }

        for columna in columnas:

            self.tabla_usuarios.heading(
                columna,
                text=encabezados[columna]
            )

        self.tabla_usuarios.column(
            "identificacion",
            width=110,
            anchor="center"
        )

        self.tabla_usuarios.column(
            "nombre",
            width=180
        )

        self.tabla_usuarios.column(
            "correo",
            width=220
        )

        self.tabla_usuarios.column(
            "usuario",
            width=120,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            contenedor_tabla,
            orient="vertical",
            command=self.tabla_usuarios.yview
        )

        self.tabla_usuarios.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tabla_usuarios.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.refrescar_usuarios()

    # =====================================================
    # REFRESCAR USUARIOS
    # =====================================================

    def refrescar_usuarios(self) -> None:

        for item in (
            self.tabla_usuarios.get_children()
        ):

            self.tabla_usuarios.delete(item)

        for usuario in (
            self.restaurante_servicio.listar_usuarios()
        ):

            self.tabla_usuarios.insert(
                "",
                tk.END,
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.correo,
                    usuario.usuario
                )
            )

    # =====================================================
    # VENTAS
    # =====================================================

    def mostrar_ventas(self) -> None:

        self.limpiar_contenido()

        tk.Label(
            self.frame_contenido,
            text="Gestión de ventas",
            bg="#f5f5f5",
            font=("Arial", 21, "bold")
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        # =================================================
        # FORMULARIO DE VENTA
        # =================================================

        formulario = tk.LabelFrame(
            self.frame_contenido,
            text="Registrar venta",
            bg="#f5f5f5",
            padx=20,
            pady=15
        )

        formulario.pack(
            fill="x",
            pady=(0, 15)
        )

        formulario.columnconfigure(
            1,
            weight=1
        )

        # =================================================
        # USUARIO
        # =================================================

        tk.Label(
            formulario,
            text="Usuario",
            bg="#f5f5f5"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=8
        )

        opciones_usuarios = (
            self.obtener_opciones_usuarios_venta()
        )

        self.usuario_venta_combo = ttk.Combobox(
            formulario,
            values=list(
                opciones_usuarios.keys()
            ),
            state="readonly"
        )

        self.usuario_venta_combo.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=8
        )

        # =================================================
        # PRODUCTO
        # =================================================

        tk.Label(
            formulario,
            text="Producto",
            bg="#f5f5f5"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=8
        )

        opciones_productos = (
            self.obtener_opciones_productos_venta()
        )

        self.producto_venta_combo = ttk.Combobox(
            formulario,
            values=list(
                opciones_productos.keys()
            ),
            state="readonly"
        )

        self.producto_venta_combo.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=8
        )

        # =================================================
        # BOTÓN REGISTRAR VENTA
        # =================================================

        acciones = tk.Frame(
            formulario,
            bg="#f5f5f5"
        )

        acciones.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(12, 0)
        )

        self.crear_boton_oscuro(
            acciones,
            "Registrar venta",
            "sales",
            self.registrar_venta
        ).pack(
            fill="x"
        )

        # =================================================
        # TABLA DE VENTAS
        # =================================================

        listado = tk.LabelFrame(
            self.frame_contenido,
            text="Ventas registradas",
            padx=10,
            pady=10
        )

        listado.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "venta",
            "usuario",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            listado,
            columns=columnas,
            show="headings"
        )

        self.tabla_ventas.heading(
            "venta",
            text="Venta"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.column(
            "venta",
            width=80,
            anchor="center"
        )

        self.tabla_ventas.column(
            "usuario",
            width=220
        )

        self.tabla_ventas.column(
            "producto",
            width=260
        )

        self.tabla_ventas.column(
            "fecha",
            width=120,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            listado,
            orient="vertical",
            command=self.tabla_ventas.yview
        )

        self.tabla_ventas.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tabla_ventas.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.refrescar_ventas()

    # =====================================================
    # OPCIONES USUARIOS PARA VENTAS
    # =====================================================

    def obtener_opciones_usuarios_venta(
        self
    ) -> dict:

        self.opciones_usuarios_venta = {
            (
                f"{usuario.identificacion} - "
                f"{usuario.nombre}"
            ): usuario.identificacion

            for usuario in (
                self.restaurante_servicio.listar_usuarios()
            )
        }

        return self.opciones_usuarios_venta

    # =====================================================
    # OPCIONES PRODUCTOS PARA VENTAS
    # =====================================================

    def obtener_opciones_productos_venta(
        self
    ) -> dict:

        self.opciones_productos_venta = {
            (
                f"{producto.codigo} - "
                f"{producto.nombre}"
            ): producto.codigo

            for producto in (
                self.restaurante_servicio.listar_productos()
            )
        }

        return self.opciones_productos_venta

    # =====================================================
    # REGISTRAR VENTA
    # =====================================================

    def registrar_venta(self) -> None:

        usuario_seleccionado = (
            self.usuario_venta_combo.get()
        )

        producto_seleccionado = (
            self.producto_venta_combo.get()
        )

        usuario_id = (
            self.opciones_usuarios_venta.get(
                usuario_seleccionado,
                ""
            )
        )

        producto_codigo = (
            self.opciones_productos_venta.get(
                producto_seleccionado,
                ""
            )
        )

        try:

            self.restaurante_servicio.registrar_venta(
                usuario_id,
                producto_codigo
            )

            self.limpiar_formulario_venta()
            self.refrescar_ventas()

            messagebox.showinfo(
                "Ventas",
                "Venta registrada correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Ventas",
                str(error)
            )

    # =====================================================
    # LIMPIAR FORMULARIO VENTA
    # =====================================================

    def limpiar_formulario_venta(self) -> None:

        self.usuario_venta_combo.set("")
        self.producto_venta_combo.set("")

    # =====================================================
    # REFRESCAR VENTAS
    # =====================================================

    def refrescar_ventas(self) -> None:

        for item in (
            self.tabla_ventas.get_children()
        ):

            self.tabla_ventas.delete(item)

        for venta in (
            self.restaurante_servicio.listar_ventas()
        ):

            usuario = (
                self.restaurante_servicio
                .buscar_usuario_por_identificacion(
                    venta.usuario_id
                )
            )

            producto = (
                self.restaurante_servicio
                .buscar_producto_por_codigo(
                    venta.producto_codigo
                )
            )

            if usuario is None:

                texto_usuario = venta.usuario_id

            else:

                texto_usuario = (
                    f"{usuario.identificacion} - "
                    f"{usuario.nombre}"
                )

            if producto is None:

                texto_producto = venta.producto_codigo

            else:

                texto_producto = (
                    f"{producto.codigo} - "
                    f"{producto.nombre}"
                )

            self.tabla_ventas.insert(
                "",
                tk.END,
                values=(
                    venta.identificador,
                    texto_usuario,
                    texto_producto,
                    venta.fecha
                )
            )

    # =====================================================
    # CERRAR SESIÓN
    # =====================================================

    def cerrar_sesion(self) -> None:

        self.al_cerrar_sesion()