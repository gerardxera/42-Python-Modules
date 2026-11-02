#!/usr/bin/python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    file_data: typing.IO[str] | None = None
    text: str = ""

    try:
        file_data = open(file_name, "r")
        text = file_data.read()
        print("---")
        print(text, end="")
        print("---")

    except FileNotFoundError as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    except PermissionError as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    except IsADirectoryError as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    finally:
        if file_data is not None:
            file_data.close()
            print(f"File '{file_name}' closed.")

    print("Transform data:")
    transform_text: str = text.replace("\n", "#\n")
    print("---")
    print(transform_text, end="")
    print("---")

    new_name: str = input("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_name}'")
    new_data: typing.IO[str] | None = None

    try:
        new_data = open(new_name, "w")
        new_data.write(transform_text)
        print(f"Data saved in file '{new_name}'.")
    except FileNotFoundError as error:
        print(f"Error opening file '{new_name}': {error}")
    except PermissionError as error:
        print(f"Error opening file '{new_name}': {error}")
    except IsADirectoryError as error:
        print(f"Error opening file '{new_name}': {error}")
    finally:
        if new_data is not None:
            new_data.close()


if __name__ == "__main__":
    main()
