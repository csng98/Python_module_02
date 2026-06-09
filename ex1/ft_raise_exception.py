def input_temperature(temp_str: str) -> int:
    print(f"Input data is: '{temp_str}'")
    try:
        temp_int = int(temp_str)
    except ValueError:
        raise ValueError(f"Caught input_temperature error: invalid "
              f"literal for int() with base 10: '{temp_str}'\n")
    if temp_int < 0:
        raise ValueError(f"Caught input_temperature error: {temp_str}°C"
              f" is too cold for plants (min 0°C)\n")
    if temp_int > 40:
        raise ValueError(f"Caught input_temperature error: {temp_str}°C"
              f" is too hot for plants (max 40°C)\n")
    print(f"Temperature is now {temp_str}°C\n")
    return temp_int


def test_temperature() -> None:
    tests = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature ===\n")
    for t in tests:
        try:
            input_temperature(t)
        except ValueError as e:
            print(e)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
