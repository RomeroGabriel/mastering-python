# Modules and Packages

## Modules

In Python, a module is essentially a file that contains various definitions and statements. The module name corresponds to the file name without the .py extension. Within a module, the module's name (as a string) is available as the value of the global variable `__name__`.

When importing modules, if the imported **module names are placed at the top level of a file** (outside any function or class), **they are added to the module's global namespace**. This allows easy access to the functions, variables, or classes defined within the imported modules.

In addition to Python-written modules, you can also **define a folder as a module** by including a file called **init.py within it**. This folder then becomes a module that can be imported and utilized.

```python title="modules.py"
# import module 'dataclasses' to current namespaces
import dataclasses
# import names (dataclass, field) to current namespaces
from dataclasses import dataclass, field 
# import all names from the module,
# except those beginning with underscore on the name
from dataclasses import *
```

### Absolute imports

An absolute import refers to a type of import where the **location of the classes being imported is fully specified**. This allows for a clear and unambiguous reference to the desired import location, **ensuring that there is no confusion or conflict with other modules or classes that may have the same name** but reside in different packages or directories.

```python title="abs_import.py"
# from PACKAGE.MODULE.MODULE import CLASS
from pandas.core.frame import DataFrame

# import PACKAGE.MODULE.MODULE
import pandas.core.frame as frame
example = frame.DataFrame()

# from PACKAGE.MODULE import MODULE 
from pandas.core import frame
```

### Relative imports

Relative imports allow us to specify the location of the classes **being imported relative to the current package or module**. By using relative import statements, we can reference and import classes from modules **located within the same package or subpackages**, providing a concise and context-aware way to import and utilize code within the project's structure.

- Current directory: `.`
- Previous directory: `..`

<pre>
└── not_nice_import.py
    ├── relative_import.py
    ├── nice_file.py
</pre>

```python title="relative_import.py"
# if the files are in the same place
from .nice_file import add_func

# if the file calling is one directory down
from ..not_nice_import import not_nice_add_func
```

### Impact of init file

<pre>
└── src
    └── calculator_func
        ├── __init_.py
        ├── add_func.py
        ├── sub_func.py
        ├── mul_func.py
        ├── div_func.py
    ├── calculator.py
</pre>

```python title="__init__.py"
from .add_func import add_func
from .sub_func import sub_func
from .mul_func import mul_func
from .div_func import div_func
```

```python title="calculator.py"
# instead of
from calculator_func.add_func import add_func
from calculator_func.sub_func import sub_func
# possible to import
from calculator_func import add_func, sub_func, mul_func, div_func
```

### Executing modules as scripts

In Python, any file that contains a **module is also considered a Python script and can be executed when imported**. However, by including the following code block, **it prevents the module from executing when imported**, allowing the file to be used both as a **standalone script and as an importable module**:

```python title="import_main.py"
if __name__ == "__main__":
    # Code to be executed when the script is run directly
    pass
```

This usage of the `__name__` variable ensures that the **code block under the if statement is only executed when the file is run directly as a script**, rather than being imported as a module. This distinction allows the file to serve dual purposes, functioning as an executable script or an importable module based on how it is invoked.

## Packages

In Python, a package is a **collection of modules** that enables hierarchical structuring of the module namespace using dot notation. They help **prevent naming collisions between modules** by providing a way to create a nested structure for modules. Similar to how modules mitigate conflicts in global variable names, packages ensure that module names remain distinct and avoid clashes within the project's namespace. This hierarchical organization enhances code readability, maintainability, and reduces the risk of naming conflicts.

### Difference when use `from` and `import`

```python title="from_import.py"
# item can be either a submodule, or some other name defined in the package,
# like a function, class or variable
from package import item

# item MUST BE a package. subitem can be a module or a package
# but can't be a class or function
import package.item.subitem
```

### Importing * from a Package

Importing everything using the `*` notation in Python packages can lead to **lengthy import times and unintended side effects**. It is generally **not recommended** to import all modules from a package in this manner. However, **you can specify which modules should be imported** when using `from package import *`, you can define a list named `__all__` in the `__init__`.py file of the package.

```python title="__init__with_all.py"
from .add_func import add_func
from .sub_func import sub_func
from .mul_func import mul_func
from .div_func import div_func
__all__ = [
    "add_func",
    "sub_func",
    "mul_func",
    "div_func",
]
```

## References

- [Python Modules doc](https://docs.python.org/3/tutorial/modules.html)
- [Real Python Modules and Packages](https://realpython.com/python-modules-packages/)
