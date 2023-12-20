import itertools

consonants = ['d', 'f', 'k', 'l', 'n', 'p']
vowels = ['a', 'e', 'i', 'o', 'u']

gen_obj = itertools.chain(consonants, vowels)

print(list(gen_obj))