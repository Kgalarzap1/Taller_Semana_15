import json
from pathlib import Path


class ArchivoServicio:

    def __init__(
        self,
        carpeta_datos
    ) -> None:

        self.carpeta_datos = Path(
            carpeta_datos
        )

    def leer_json(
        self,
        nombre_archivo: str
    ) -> list:

        ruta = (
            self.carpeta_datos
            / nombre_archivo
        )

        try:

            with ruta.open(
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(
                    archivo
                )

            if not isinstance(
                datos,
                list
            ):
                raise ValueError(
                    f"{nombre_archivo} "
                    "debe contener una lista."
                )

            return datos

        except FileNotFoundError:

            return []

        except json.JSONDecodeError as error:

            raise ValueError(
                f"El archivo {nombre_archivo} "
                "contiene un JSON inválido."
            ) from error

    def escribir_json(
        self,
        nombre_archivo: str,
        datos: list
    ) -> None:

        ruta = (
            self.carpeta_datos
            / nombre_archivo
        )

        with ruta.open(
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                ensure_ascii=False,
                indent=4
            )