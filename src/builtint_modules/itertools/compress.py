import itertools

str_exe = "ABCDEFGH"
num = (True, False, True, True, False, True)

gen_obj = itertools.compress(str_exe, num)

print(list(gen_obj))