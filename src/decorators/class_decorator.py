from typing import Any


class nice_logger:
    def __init__(self, string_log = "") -> None:
        self.string_log = string_log

    def __call__(self, func) -> Any:
        def logger(*_args):
            result = func(*_args)
            if self.string_log:
                print(f"{self.string_log}: {result}")
            return result
        return logger

@nice_logger(string_log="F1: The final result is ")
def f1(num1):
    return 10 + num1

f1(10)