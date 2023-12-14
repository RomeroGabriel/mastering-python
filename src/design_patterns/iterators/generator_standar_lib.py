import itertools

int_gen = itertools.count(1, .5)

print(f"1º CALL: {next(int_gen)}")
print(f"2º CALL: {next(int_gen)}")
print(f"3º CALL: {next(int_gen)}")
print(f"4º CALL: {next(int_gen)}")