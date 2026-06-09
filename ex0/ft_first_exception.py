def input_temperature(temp_str: str) -> int:
    print(f"Input data is: '{temp_str}'")
    try:
        temp_int = int(temp_str)
        print(f"Temperature is now {temp_int}°C\n")
        return temp_int
    except ValueError:
        print(f"Caught input_temperature error: invalid "
              f"literal for int() with base 10: '{temp_str}'\n")
        return -1


def test_temperature() -> None:
    tests = ["25", "abc"]
    print("=== Garden Temperature ===\n")
    for t in tests:
        input_temperature(t)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
