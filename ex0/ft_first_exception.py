def input_temperature(temp_str: str) -> int:
    print(f"Input data is: '{temp_str}'")
    return int(temp_str)


def test_temperature() -> None:
    tests = ["25", "abc"]
    print("=== Garden Temperature ===\n")
    for t in tests:
        try:
            temp_int = input_temperature(t)
            print(f"Temperature is now {temp_int}°C\n")
        except ValueError:
            print(f"Caught input_temperature error: invalid "
                  f"literal for int() with base 10: '{t}'\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
