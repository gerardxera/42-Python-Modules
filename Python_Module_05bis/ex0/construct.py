#!/usr/bin/python3

import os
import sys
import site


def main() -> None:
    '''Comprobar si estamos en un entorno virtual con bool indica si SI o NO'''
    in_venv: bool = sys.prefix != sys.base_prefix

    if not in_venv:
        print("\nLABORATORY STATUS: You are working in the open\n")
        '''indica la ruta de la version de python actual'''
        print(f"Current Python: {sys.executable}")
        '''Detectar el entorno virtual'''
        print("Virtual Environment: None detected\n")
        '''Alerta de seguridad'''
        print(
            "WARNING: You are in the global environment!\n"
            "Every reagent you install here leaks into the whole system.\n"
        )
        '''Como construir el entorno virtual y activarlo'''
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        '''Se pone delante r para ignorar les contra barras '''
        print(r"lab_env\Scripts\activate # On Window" + "\n")
        print("Then run this program again.")
    else:
        name_venv: str = os.path.basename(sys.prefix)
        '''Entorno correcto'''
        print("\nLABORATORY STATUS: The laboratory is sealed\n")
        '''indica la ruta del contenedor'''
        print(f"Current Python: {sys.executable}")
        '''Detectar el entorno virtual'''
        print(f"Virtual Environment: {name_venv}")
        print(f"Environment Path: {sys.prefix}\n")
        print(
            "SUCCESS: You are working in an isolated environment!\n"
            "Safe to install reagents without affecting the global system.\n"
        )
        '''Ruta donde pip instala los paquetes dentro del venv'''
        site_pkg: str = site.getsitepackages()[0]
        print(f"Reagent installation path: {site_pkg}")


if __name__ == "__main__":
    main()
