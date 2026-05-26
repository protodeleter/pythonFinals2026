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
            return False

    @staticmethod
    def validate_name(value):
        if value == '' or not Validator.minimum_length(value, 2):
            print("String must be greater than 2 characters")
            return False
        return True

    @staticmethod
    def validate_positive_numbers( value) -> float | bool:
        try:
            return float(value) > 0
        except exceptions.CargoWeightPositiveError:
            print("Value is not a positive number")
            return False
