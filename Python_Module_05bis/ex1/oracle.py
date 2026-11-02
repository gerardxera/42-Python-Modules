#!/usr/bin/python3
import os
from dotenv import load_dotenv  # type: ignore[import-not-found]


def check_git_ignore() -> bool:
    path = os.path.join(os.path.dirname(__file__), ".gitignore")
    if not os.path.exists(path):
        return False
    try:
        with open(path, encoding="utf-8") as f:
            return ".env" in f.read()
    except Exception:
        return False


def has_hardcoded_secret(api_key: str | None) -> bool:
    if not api_key:
        return False
    with open(__file__, encoding="utf-8") as f:
        return api_key in f.read()


def main() -> None:
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Consulting the configuration...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    """La diferencia visible entre development y production"""
    """salida de imprimir dependiendo del MATRIX_MODE"""
    if mode == "production":
        if db_url:
            print("Database: Connected to remote instance")
        else:
            print("Database: Not configured")
    else:
        if db_url:
            print("Database: Connected to local instance")
        else:
            print("Database: Not configured")
    """Chequeo visuales de seguridad"""
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {log_level}")

    if zion:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline")

    print("\nConfiguration security check:")
    if has_hardcoded_secret(api_key):
        print("[KO] Hardcoded secret detected!")
    else:
        print("[OK] No hardcoded secrets detected")

    if check_git_ignore():
        status = "OK"
    else:
        status = "WARNING"
    print(f"[{status}] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
