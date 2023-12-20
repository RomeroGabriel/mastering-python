import itertools

gen_obj = itertools.zip_longest('ABC', range(5))
print(list(gen_obj))
gen_obj = itertools.zip_longest('ABC', range(5), fillvalue="!!!")
print(list(gen_obj))
