import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class AplicacionRestaurante:

    def __init__(self) -> None:

        self.root = tk.Tk()

        self.root.title(
            "Restaurante App - Semana 15"
        )

        self.root.geometry(
            "1050x650"
        )

        self.root.minsize(
            900,
            600
        )

        ruta_base = (
            Path(__file__).resolve().parent
        )

        archivo_servicio = ArchivoServicio(
            ruta_base / "datos"
        )

        self.restaurante_servicio = (
            RestauranteServicio(
                archivo_servicio
            )
        )

        self.vista_actual = None

        self.mostrar_login()

    def cambiar_vista(
        self,
        nueva_vista
    ) -> None:

        if self.vista_actual is not None:

            self.vista_actual.destroy()

        self.vista_actual = nueva_vista

        self.vista_actual.pack(
            fill="both",
            expand=True
        )

    def mostrar_login(self) -> None:

        vista = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_main
        )

        self.cambiar_vista(
            vista
        )

    def mostrar_main(
        self,
        usuario_actual
    ) -> None:

        vista = MainView(
            self.root,
            self.restaurante_servicio,
            usuario_actual,
            self.mostrar_login
        )

        self.cambiar_vista(
            vista
        )

    def ejecutar(self) -> None:

        self.root.mainloop()


if __name__ == "__main__":

    aplicacion = AplicacionRestaurante()

    aplicacion.ejecutar()