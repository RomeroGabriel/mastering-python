import itertools


def vowel(c: str):
    return c.upper() in "AEIOU"

letters = "AEIGJIOU"
gen_obj = itertools.filterfalse(vowel, letters)

print(list(gen_obj))