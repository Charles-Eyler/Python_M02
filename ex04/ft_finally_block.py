class GardenError(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self) -> str:
        return self._msg


class PlantError(GardenError):
    def __init__(self, msg):
        super().__init__(msg)


def water_plant(plant_name) -> None:
    cap_name = str.capitalize(plant_name)
    if plant_name == cap_name:
        print(f"Watering {plant_name}: [OK]")
    else:
        msg = f"Invalid name to water: '{plant_name}'"
        raise PlantError(msg)


def test_watering_system() -> None:
    print("Opening watering system")
    i = 0
    while i < 2:
        if i == 0:
            print("Testing valid plants...")
            try:
                water_plant("Tomato")
                water_plant("Lettuce")
                water_plant("Carrots")
            except PlantError as e:
                print("Caugth PlantError:", e)
                print(".. ending tests and returning to main")
            finally:
                print("Closing watering system\n")
        if i == 1:
            print("Testing valid plants...")
            try:
                water_plant("Tomato")
                water_plant("lettuce")
                water_plant("carrots")
            except PlantError as e:
                print("Caugth PlantError:", e)
                print(".. ending tests and returning to main")
                break
            finally:
                print("Closing watering system\n")
        i += 1


def ft_finally_block() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    ft_finally_block()
