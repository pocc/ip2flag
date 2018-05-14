# Each unicode flag consists of two special country code characters (per ISO 3166-1) in combination (e.g. 🇺🇸 for United States).
# This file will print each one of those special characters.
from string import ascii_uppercase
for letter in ascii_uppercase:
    print(unichr(ord(letter)+127397) + ":" + str(hex(ord(letter)+127397)))
