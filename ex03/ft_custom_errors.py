class GardenError(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self) -> str:
        return self._msg


class PlantError(GardenError):
    def __init__(self, msg):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg):
        super().__init__(msg)


def plant_error(msg="The tomato plant is wilting!") -> None:
    raise PlantError(msg)


def water_error(msg="Not enough water in the tank!") -> None:
    raise WaterError(msg)


def testing_plant_error() -> None:
    print("Testing Plant Error...")
    try:
        plant_error()
    except PlantError as e:
        print(f"Caugth PlantError: {e}\n")


def testing_water_error() -> None:
    print("Testing Water Error...")
    try:
        water_error()
    except WaterError as e:
        print(f"Caugth WaterError: {e}\n")


def testing_garden_error() -> None:
    print("Testing GardenError...")
    i = 0
    while i < 2:
        if i == 0:
            try:
                plant_error()
            except GardenError as e:
                print("Caugth GardenError:", e)
        if i == 1:
            try:
                water_error()
            except GardenError as e:
                print("Caugth GardenError:", e)
        i += 1


def testing_all() -> None:
    print("=== Garden Error Demo ===\n")
    testing_plant_error()
    testing_water_error()
    testing_garden_error()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    testing_all()
