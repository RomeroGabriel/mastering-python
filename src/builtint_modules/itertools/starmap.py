import itertools
import operator

data = [(2,3), (4,5), (6,2)]
gen_obj = itertools.starmap(operator.mul, data)

print(list(gen_obj))
