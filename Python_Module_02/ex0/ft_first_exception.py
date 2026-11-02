#!/usr/bin/python


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_inputs = ["25", "abc"]

    for data in test_inputs:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}\n")


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
