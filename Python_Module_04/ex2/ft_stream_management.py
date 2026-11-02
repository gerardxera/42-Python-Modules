#!/usr/bin/python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
        print(
            f"[STDERR] Error opening file '{file_name}': {error}",
            file=sys.stderr
        )
        return
    except PermissionError as error:
        print(
            f"[STDERR] Error opening file '{file_name}': {error}",
            file=sys.stderr
        )
        return
    except IsADirectoryError as error:
        print(
            f"[STDERR] Error opening file '{file_name}': {error}",
            file=sys.stderr
        )
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

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    user_input: str = sys.stdin.readline()
    new_name: str = user_input.rstrip("\n")
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
        print(
            f"[STDERR] Error opening file '{new_name}': {error}",
            file=sys.stderr
        )
        print("Data not saved.")
    except PermissionError as error:
        print(
            f"[STDERR] Error opening file '{new_name}': {error}",
            file=sys.stderr
        )
        print("Data not saved.")
    except IsADirectoryError as error:
        print(
            f"[STDERR] Error opening file '{new_name}': {error}",
            file=sys.stderr
        )
        print("Data not saved.")
    finally:
        if new_data is not None:
            new_data.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user Ctrl + C.")
