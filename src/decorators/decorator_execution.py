decorator_log = []

def decorator_func(func):
    decorator_log.append(func)
    print(f"Executing decorator!! COUNT: {decorator_log}")
    return func

@decorator_func
def f1():
    print("F1 execution!!")

@decorator_func
def f2():
    print("F2 execution!!")

def f3():
    print("F3 execution!!")

def main():
    print("Starting MAIN!")
    print(f"decorator_log on MAIN -> {decorator_log}")
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()