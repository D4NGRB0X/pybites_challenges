import string

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
   """Receives input string and checks if all chars are
   VOWELS. Match is case insensitive."""
   vowel_chars = True
   for char in input_str.lower():
      if char not in VOWELS:
         vowel_chars = False
   return vowel_chars
          


def contains_any_py_chars(input_str):
   """Receives input string and checks if any of the PYTHON
   chars are in it. Match is case insensitive."""
   py_chars = False
   for char in input_str.lower():
      if char in PYTHON:
         py_chars = True
   return py_chars


def contains_digits(input_str):
   """Receives input string and checks if it contains
   one or more digits."""
   has_digit = False
   for char in input_str:
      if char in string.digits:
         has_digit = True
   return has_digit