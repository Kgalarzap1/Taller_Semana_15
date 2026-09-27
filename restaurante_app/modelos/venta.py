class Venta:

    def __init__(
        self,
        identificador: str,
        usuario_id: str,
        producto_codigo: str,
        fecha: str
    ) -> None:

        self.identificador = self.validar_texto(
            identificador,
            "identificador"
        )

        self.usuario_id = self.validar_texto(
            usuario_id,
            "usuario"
        )

        self.producto_codigo = self.validar_texto(
            producto_codigo,
            "producto"
        )

        self.fecha = self.validar_texto(
            fecha,
            "fecha"
        )

    @staticmethod
    def validar_texto(
        valor: str,
        campo: str
    ) -> str:

        if not valor or not valor.strip():
            raise ValueError(
                f"El campo {campo} no puede estar vacío."
            )

        return valor.strip()

    def a_diccionario(self) -> dict:

        return {
            "identificador": self.identificador,
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha
        }

    def __str__(self) -> str:

        return (
            f"{self.identificador} | "
            f"{self.usuario_id} | "
            f"{self.producto_codigo} | "
            f"{self.fecha}"
        )