def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()
    if type(value) not in [float, int]:
        raise TypeError

    if fmt.lower() not in ["cm", "in"]:
        raise ValueError

    conversion = 0
    if fmt == "in":
        conversion = value / 2.54

    if fmt == "cm":
        conversion = value * 2.54

    return round(conversion, 4)
