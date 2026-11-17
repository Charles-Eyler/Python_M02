valid_input = "25"
invalid_input = "abc"
extreme_high_temp = "100"
extreme_low_temp = "-50"


def test_temperature(temp_str) -> None:
    while True:
        try:
            valid_input = input_temperature(temp_str)
            if valid_input < 0:
                raise ValueError(f"{valid_input}°C is too low "
                                 "for plants (min 0°C)")
            if valid_input > 40:
                raise ValueError(f"{valid_input}°C is too high "
                                 "for plants (max 100°C)")
            else:
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


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature(valid_input)
    test_temperature(invalid_input)
    test_temperature(extreme_high_temp)
    test_temperature(extreme_low_temp)
    print("All tests completed - program didn't crash!")
