import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES[self.color.upper()] if self.color.upper() in COLOR_NAMES.keys() else None

    @staticmethod
    def hex2rgb(hex_code):
        """Class method that converts a hex value into an rgb one"""
        if len(hex_code) < 6:
            raise ValueError
        try:
            hex_code = hex_code.strip('#')
            rgb = [int(hex_code[char_index:char_index + 2], 16) for char_index in range(0, len(hex_code), 2)]
            return tuple(rgb)
        except:
            raise ValueError

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        for i in rgb:
            if i not in range(0, 256):
                raise ValueError
        try:
            hex_chars = "".join([hex(val)[2:].zfill(2) for val in rgb])
            return f"#{hex_chars}"
        except:
            raise ValueError

    def __repr__(self):
        return f"Color('{self.color}')"

    def __str__(self):
        if self.rgb is not None:
            return f"{self.rgb}"
        return "Unknown"
