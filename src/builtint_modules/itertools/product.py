import itertools

gen_obj = itertools.product("ABC", range(2))
print(list(gen_obj))

gen_obj = itertools.product("ABC", repeat=2)
print(list(gen_obj))