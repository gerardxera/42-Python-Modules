#!/usr/bin/python


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    test_inputs = ["25", "abc", "100", "-50"]

    for data in test_inputs:
        print(f"Input data is '{data}'")

        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}\n")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
