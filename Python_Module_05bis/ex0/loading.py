#!/usr/bin/python3
import importlib
import importlib.util


def check_install(module_name: str) -> tuple[bool, str]:
    """Comprueba si un módulo libreria está instalado y devuelve su versión."""
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        """El modulo no esta instalado"""
        return False, ""
    try:
        """Si el modulo existe lo importamos con su nombre de texto"""
        module = importlib.import_module(module_name)
        """Si Leemos el atributo __version__ de forma segura"""
        version = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, ""


def main() -> None:
    print("REAGENT STATUS: Loading reagents...i\n")
    print("Checking dependencies:")

    module_name = ["pandas", "numpy"]
    missing: list[str] = []

    for name in module_name:
        installed, ver = check_install(name)
        if installed:
            if name == "pandas":
                desc = "Data manipulation ready"
            else:
                desc = "Numerical computation ready"
            print(f"[ok] {name} ({ver}) - ({desc})")
        else:
            missing.append(name)
            print(f"[MISSING] {name} is not installed.")

    print()
    print("pip vs Poetry:")
    print(
        "requirements.txt declares what to install; "
        "pip resolves it at install time."
    )
    print(
        "pyproject.toml declares the same constraints, "
        "and Poetry pins the resolved "
    )
    print("versions in poetry.lock so every install is identical.\n")

    if missing:
        print("To install missing reagents:")
        print(" Using pip: pip install -r ex0/requirements.txt")
        print(" Using Poetry: poetry install")
    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
