class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown watering error"):
        super().__init__(message)


def simulate_plant_issue():
    raise PlantError("The tomato plant is wilting!")


def simulate_water_issue():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        simulate_plant_issue()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        simulate_water_issue()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        simulate_plant_issue()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        simulate_water_issue()
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
