from typing import overload, Union

@overload
def process_data(data: str) -> str:
    ...

@overload
def process_data(data: int) -> int:
    ...

def process_data(data: Union[str, int]) -> Union[str, int]:
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return data * 2
    else:
        raise ValueError("Unsupported data type")

@overload
def calculate(x: int) -> int:
    ...

@overload
def calculate(x: int, y: int) -> int:
    ...

def calculate(x, y=None):
    if y is None:
        return x * 2
    else:
        return x * y
