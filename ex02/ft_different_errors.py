
from os import open


def garden_operations(operation_number) -> None:
    if operation_number == 0:
        _ = int("abc")
    elif operation_number == 1:
        _ = 3 / 0
    elif operation_number == 2:
        _ = open("Not a file", 1, 1)
    elif operation_number == 3:
        _ = "Hello World!" + 1
    else:
        print("Operation completed succesfully\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while i <= 4:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caugth ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caugth FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        finally:
            i += 1

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
