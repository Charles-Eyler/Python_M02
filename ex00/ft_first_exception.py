valid_input = "25"
invalid_input = "abc"


def test_temperature(temp_str) -> None:
    while True:
        try:
            valid_input = input_temperature(temp_str)
            print(f"Input data is '{valid_input}'")
            print(f"Temperature is now {valid_input}°C\n")
            break
        except ValueError as e:
            print(f"Input data is '{temp_str}'")
            print("Caught input_temperature error:", e, "\n")
            break


def input_temperature(temp_str) -> int:
    user_input = int(temp_str)
    return user_input


def ft_first_exception() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature(valid_input)
    test_temperature(invalid_input)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
