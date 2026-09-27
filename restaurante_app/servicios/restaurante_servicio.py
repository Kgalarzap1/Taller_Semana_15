from datetime import date

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(
        self,
        archivo_servicio: ArchivoServicio
    ) -> None:

        self.archivo_servicio = archivo_servicio

        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

        # Índices para búsquedas rápidas
        self._indice_productos = {}
        self._indice_usuarios = {}
        self._indice_acceso = {}

        self.cargar_datos()

    # =====================================================
    # CARGA DE DATOS
    # =====================================================

    def cargar_datos(self) -> None:

        datos_productos = (
            self.archivo_servicio.leer_json(
                "productos.json"
            )
        )

        datos_usuarios = (
            self.archivo_servicio.leer_json(
                "usuarios.json"
            )
        )

        datos_ventas = (
            self.archivo_servicio.leer_json(
                "ventas.json"
            )
        )

        self._productos = [
            Producto(
                dato["codigo"],
                dato["nombre"],
                dato["categoria"],
                float(dato["precio"]),
                int(dato["stock"])
            )
            for dato in datos_productos
        ]

        self._usuarios = [
            Usuario(
                dato["identificacion"],
                dato["nombre"],
                dato["correo"],
                dato["usuario"],
                dato["contrasena"]
            )
            for dato in datos_usuarios
        ]

        self._ventas = [
            Venta(
                dato["identificador"],
                dato["usuario_id"],
                dato["producto_codigo"],
                dato["fecha"]
            )
            for dato in datos_ventas
        ]

        self._reconstruir_indices()

    # =====================================================
    # ÍNDICES
    # =====================================================

    def _reconstruir_indices(self) -> None:

        self._indice_productos = {
            producto.codigo: producto
            for producto in self._productos
        }

        self._indice_usuarios = {
            usuario.identificacion: usuario
            for usuario in self._usuarios
        }

        self._indice_acceso = {
            usuario.usuario: usuario
            for usuario in self._usuarios
        }

    # =====================================================
    # LOGIN
    # =====================================================

    def validar_acceso(
        self,
        nombre_usuario: str,
        contrasena: str
    ) -> Usuario | None:

        usuario = self._indice_acceso.get(
            nombre_usuario
        )

        if usuario is None:
            return None

        if usuario.contrasena != contrasena:
            return None

        return usuario

    # =====================================================
    # CONSULTAS
    # =====================================================

    def listar_productos(
        self
    ) -> list[Producto]:

        return list(
            self._productos
        )

    def listar_usuarios(
        self
    ) -> list[Usuario]:

        return list(
            self._usuarios
        )

    def listar_ventas(
        self
    ) -> list[Venta]:

        return list(
            self._ventas
        )

    def cantidad_productos(self) -> int:

        return len(
            self._productos
        )

    def cantidad_usuarios(self) -> int:

        return len(
            self._usuarios
        )

    def cantidad_ventas(self) -> int:

        return len(
            self._ventas
        )

    # =====================================================
    # BÚSQUEDAS
    # =====================================================

    def buscar_producto_por_codigo(
        self,
        codigo: str
    ) -> Producto | None:

        codigo = codigo.strip()

        if not codigo:
            return None

        return self._indice_productos.get(
            codigo
        )

    def buscar_usuario_por_identificacion(
        self,
        identificacion: str
    ) -> Usuario | None:

        identificacion = identificacion.strip()

        if not identificacion:
            return None

        return self._indice_usuarios.get(
            identificacion
        )

    # =====================================================
    # PERSISTENCIA DE PRODUCTOS
    # =====================================================

    def guardar_productos(self) -> None:

        datos = [
            producto.a_diccionario()
            for producto in self._productos
        ]

        self.archivo_servicio.escribir_json(
            "productos.json",
            datos
        )

    # =====================================================
    # CRUD DE PRODUCTOS
    # =====================================================

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio,
        stock
    ) -> Producto:

        codigo = codigo.strip()

        if codigo in self._indice_productos:

            raise ValueError(
                "Ya existe un producto "
                "con ese código."
            )

        try:
            precio = float(precio)

        except (ValueError, TypeError):

            raise ValueError(
                "El precio debe ser "
                "un número válido."
            )

        try:
            stock = int(stock)

        except (ValueError, TypeError):

            raise ValueError(
                "El stock debe ser "
                "un número entero."
            )

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        self._productos.append(
            producto
        )

        self._reconstruir_indices()

        self.guardar_productos()

        return producto

    # =====================================================
    # ACTUALIZAR PRODUCTO
    # =====================================================

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio,
        stock
    ) -> Producto:

        codigo = codigo.strip()

        producto_existente = (
            self._indice_productos.get(
                codigo
            )
        )

        if producto_existente is None:

            raise ValueError(
                "No existe un producto "
                "con ese código."
            )

        try:
            precio = float(precio)

        except (ValueError, TypeError):

            raise ValueError(
                "El precio debe ser "
                "un número válido."
            )

        try:
            stock = int(stock)

        except (ValueError, TypeError):

            raise ValueError(
                "El stock debe ser "
                "un número entero."
            )

        producto_actualizado = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        posicion = self._productos.index(
            producto_existente
        )

        self._productos[posicion] = (
            producto_actualizado
        )

        self._reconstruir_indices()

        self.guardar_productos()

        return producto_actualizado

    # =====================================================
    # ELIMINAR PRODUCTO
    # =====================================================

    def eliminar_producto(
        self,
        codigo: str
    ) -> Producto:

        codigo = codigo.strip()

        producto = (
            self._indice_productos.get(
                codigo
            )
        )

        if producto is None:

            raise ValueError(
                "No existe un producto "
                "con ese código."
            )

        self._productos.remove(
            producto
        )

        self._reconstruir_indices()

        self.guardar_productos()

        return producto

    # =====================================================
    # VENTAS - SEMANA 15
    # =====================================================

    def generar_identificador_venta(
        self
    ) -> str:

        siguiente = (
            len(self._ventas) + 1
        )

        return f"V{siguiente:03d}"

    # =====================================================
    # GUARDAR VENTAS
    # =====================================================

    def guardar_ventas(self) -> None:

        datos = [
            venta.a_diccionario()
            for venta in self._ventas
        ]

        self.archivo_servicio.escribir_json(
            "ventas.json",
            datos
        )

    # =====================================================
    # REGISTRAR VENTA
    # =====================================================

    def registrar_venta(
        self,
        usuario_id: str,
        producto_codigo: str
    ) -> Venta:

        usuario_id = usuario_id.strip()
        producto_codigo = producto_codigo.strip()

        # ---------------------------------------------
        # Validar selección de usuario
        # ---------------------------------------------

        if not usuario_id:

            raise ValueError(
                "Debe seleccionar un usuario."
            )

        # ---------------------------------------------
        # Validar selección de producto
        # ---------------------------------------------

        if not producto_codigo:

            raise ValueError(
                "Debe seleccionar un producto."
            )

        # ---------------------------------------------
        # Buscar usuario
        # ---------------------------------------------

        usuario = (
            self.buscar_usuario_por_identificacion(
                usuario_id
            )
        )

        if usuario is None:

            raise ValueError(
                "El usuario seleccionado "
                "no existe."
            )

        # ---------------------------------------------
        # Buscar producto
        # ---------------------------------------------

        producto = (
            self.buscar_producto_por_codigo(
                producto_codigo
            )
        )

        if producto is None:

            raise ValueError(
                "El producto seleccionado "
                "no existe."
            )

        # ---------------------------------------------
        # VERIFICAR STOCK
        # ---------------------------------------------

        if producto.stock <= 0:

            raise ValueError(
                f"No hay stock disponible de "
                f"{producto.nombre}."
            )

        # ---------------------------------------------
        # CREAR VENTA
        # ---------------------------------------------

        nueva_venta = Venta(
            self.generar_identificador_venta(),
            usuario_id,
            producto_codigo,
            date.today().isoformat()
        )

        # ---------------------------------------------
        # REGISTRAR VENTA EN MEMORIA
        # ---------------------------------------------

        self._ventas.append(
            nueva_venta
        )

        # ---------------------------------------------
        # DESCONTAR UNA UNIDAD DEL STOCK
        # ---------------------------------------------

        producto.stock = (
            producto.stock - 1
        )

        # ---------------------------------------------
        # GUARDAR CAMBIOS
        # ---------------------------------------------

        self.guardar_ventas()
        self.guardar_productos()

        return nueva_venta