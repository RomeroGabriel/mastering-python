import itertools
import operator

first10 = (1,2,3,4,5,6,7,8,9,10)
gen_obj = itertools.accumulate(first10)

print(list(gen_obj))
gen_obj = itertools.accumulate(first10, operator.mul)

print(list(gen_obj))