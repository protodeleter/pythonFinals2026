import exceptions


def minimum_length(value, length):
    """
    check if string length is greater than given length
    :param value: string
    :param length: minimum length
    :return: bool
    """
    try:
        return len(value) > length
    except exceptions.CargoNameError:
        print("String must be greater than " + str(length) + " characters")


def validate_name(value) -> str | None:
    """
    validate cargo name
    must be string and longer than 2 characters
    :param value:
    :return: string or None
    """
    try:
        name = str(value)
    except ValueError:
        return None

    if not minimum_length(value, 2):
        return None

    return name


def validate_positive_numbers(value) -> float | None:
    """
    validate positive numeric value
    :param value:
    :return: float or None
    """
    try:
        num = float(value)
    except ValueError:
        return None

    if num <= 0:
        return None

    return num


def validate_planet(value):
    """
    validate planet name
    must be non-empty string
    :param value:
    :return: string or None
    """
    planet = str(value)
    if not minimum_length(value, 1):
        return None
    return planet


def validate_danger_level(value):
    """
    validate danger level (1–5)
    :param value:
    :return: int or None
    """
    try:
        value = int(value)
    except ValueError:
        return None

    if value < 1 or value > 5:
        return None

    return value


def validate_cooling_level(value):
    """
    validate cooling requirement (0 or 1)
    :param value:
    :return: int or None
    """
    try:
        value = int(value)
    except ValueError:
        return None

    if value < 0 or value > 1:
        return None

    return value