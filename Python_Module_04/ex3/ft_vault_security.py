#!/usr/bin/python3


def secure_archive(
        file_name: str,
        action: str = "read",
        content: str = ""
        ) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as file_data:
                return (True, file_data.read())
        elif action == "write":
            with open(file_name, "w") as file_data:
                file_data.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action: '{action}'."
                           "Use 'read' for reading or 'write' for writing")
    except FileNotFoundError as error:
        return False, str(error)
    except PermissionError as error:
        return False, str(error)


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read", ""))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read", ""))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "read", "")
    print(result)
    data: str = ""
    if result[0]:
        data = result[1]
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", data))


if __name__ == "__main__":
    main()
