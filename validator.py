import exceptions


class Validator:
    def __init__(self):
        pass

    def only_numbers(self, value):
        pass

    @staticmethod
    def minimum_length(value, length):

        try:
            return len(value) > length
        except exceptions.CargoNameError:
            print("String must be greater than " + str(length) + " characters")

    @staticmethod
    def validate_name(value):

        try:
            name = str(value)
        except ValueError:
            raise exceptions.CargoNameError("Cargo name must be a string")
        if not Validator.minimum_length(value, 2):
            raise exceptions.CargoNameError("Cargo name must be longer than " + str(2) + " characters")
        return name


    @staticmethod
    def validate_positive_numbers( value) -> float | bool:
        try:
            weight = float(value)
        except ValueError:
            raise exceptions.CargoWeightPositiveError("Cargo weight must be a number")

        if weight < 0:
            raise exceptions.CargoWeightPositiveError("Cargo weight must be a positive number")
        return weight


    @staticmethod
    def validate_planet(value):
        if not isinstance(value, str):
            raise ValueError("Planet must be a string")

        value = value.strip()

        if not Validator.minimum_length(value, 1):
            raise ValueError("Planet must not be empty")

        return value

    @staticmethod
    def validate_danger_level( value):

        try:
            value = int(value)
        except ValueError:
            print("Danger level must be a number")

        if int(value) < 0 or int(value) > 5 :
            raise ValueError("Danger level must be between 0 and 5")
        return value
    @staticmethod
    def validate_cooling_level( value):
        try:
            value = int(value)
        except ValueError:
            print("Cooling level must be a number")
        if int(value) < 0 or int(value) > 1:
            raise ValueError("Cooling level must be between 0 and 1")
        return value