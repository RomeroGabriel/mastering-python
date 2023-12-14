import itertools

nums = (0,1,2,3,4,5,6,7,8,9)

gen_obj = itertools.islice(nums, 4)

print(list(gen_obj))
gen_obj = itertools.islice(nums, 4, 7)

print(list(gen_obj))

gen_obj = itertools.islice(nums, 1, 7, 2)

print(list(gen_obj))