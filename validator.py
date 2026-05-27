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
    def validate_name(value) -> str | None:
        try:
            name = str(value)
        except ValueError:
            return None
        if not Validator.minimum_length(value, 2):
            return None
        return name


    @staticmethod
    def validate_positive_numbers( value) -> float | None:
        try:
            num = float(value)
        except ValueError:
            return None
        if num <= 0:
            return None
        return num


    @staticmethod
    def validate_planet(value):
        planet = str(value)
        if not Validator.minimum_length(value, 1):
            return None
        return planet

    @staticmethod
    def validate_danger_level( value):

        try:
            value = int(value)
        except ValueError:
            return None

        if value < 1 or value > 5:
            return None

        return value
    @staticmethod
    def validate_cooling_level( value):
        try:
            value = int(value)
        except ValueError:
            return None
        if int(value) < 0 or int(value) > 1:
            return None
        return value