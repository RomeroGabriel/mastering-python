import itertools


def check_first5(num):
    return num in (0,1,2,3,4,5)

first10 = (0,1,2,3,4,5,6,7,8,9,10)
gen_obj = itertools.takewhile(check_first5, first10)

print(list(gen_obj))