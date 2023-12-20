import itertools

vowels = ['a', 'e', 'i', 'o', 'u']

gen_obj = itertools.chain.from_iterable(enumerate(vowels))

print(list(gen_obj))