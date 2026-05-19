class Validator:
    def __init__(self):
        pass

    def only_numbers(self, value):
        pass

    @staticmethod
    def minimum_length(value, length):

        if len(value) < length:
            return False
        return True

    @staticmethod
    def validate_positive_numbers( value):
        try:
            return float(value) > 0
        except ValueError:
            return False
