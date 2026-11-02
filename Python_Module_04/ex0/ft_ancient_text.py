#!/usr/bin/python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    file_data: typing.IO[str] | None = None

    try:
        file_data = open(file_name, "r")
        text: str = file_data.read()
        print("---")
        print(text, end="")
        print("---")

    except FileNotFoundError as error:
        print(f"Error opening file '{file_name}': {error}")
    except PermissionError as error:
        print(f"Error opening file '{file_name}': {error}")
    except IsADirectoryError as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if file_data is not None:
            file_data.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
