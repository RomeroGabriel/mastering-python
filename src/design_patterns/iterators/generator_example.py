def test_gen():
    print("Start test gen")
    yield 1
    print("After yield 1")
    yield 2
    print("Finish test gen")

for t in test_gen():
    print(f"---> {t}")