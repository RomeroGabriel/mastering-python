# Design Patterns

> Base information resource: [Refactoring Guru](https://refactoring.guru/design-patterns/catalog)

`It's important to note that not every design pattern is applicable to every programming language`. In Python, for example, some design patterns are embedded in the language itself. For instance, the Iterator design pattern can be implemented using generators in Python.

## Strategy with First-Class Functions

> Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

In Python, strategy pattern can be simpler using functions as first-class objects.

??? note "Example Description"
    ## Consider an online store with these discount rules:

    1. Customers with 1,000 or more fidelity points receive a 5% discount on their entire order.
    1. A 10% discount is applied to each line item that contains 20 or more units in the same order.
    1. Orders with at least 10 distinct items receive a 7% discount on the entire order.

    ### Context
    Context refers to the `service provided, which delegates some of its computation to interchangeable components that implement different discount algorithms`. In the ecommerce example, the context is represented by an `Order`, and it can be configured to apply a promotional discount based on one of several algorithms.

    ### Strategy
    The `common interface shared among the components that implement` these different discount algorithms. In the ecommerce example, use an abstract class called `Promotion` to fulfill this role.

    ### Concrete Strategy
    Refers to one of the specific implementations of the Strategy interface. In the ecommerce example, there are three concrete strategies: `FidelityPromo`, `BulkPromo`, and `LargeOrderPromo`.

??? example "Function-Oriented Strategy"

    ```pycon exec="1" source="console"  title="func_strategy.py"
    >>> from collections.abc import Sequence
    >>> from dataclasses import dataclass
    >>> from decimal import Decimal
    >>> from typing import Optional, Callable, NamedTuple
    ... ...
    >>> class Customer(NamedTuple):
    ...     name: str
    ...     fidelity: int
    ... ...
    >>> class LineItem(NamedTuple):
    ...     product: str
    ...     quantity: int
    ...     price: Decimal
    ...     def total(self):
    ...         return self.price * self.quantity
    ... ...
    >>> @dataclass(frozen=True)
    >>> class Order:  # the Context
    ...     customer: Customer
    ...     cart: Sequence[LineItem]
    ...     promotion: Optional[Callable[['Order'], Decimal]] = None
    ...     def total(self) -> Decimal:
    ...         totals = (item.total() for item in self.cart)
    ...         return sum(totals, start=Decimal(0))
    ...     def due(self) -> Decimal:
    ...         if self.promotion is None:
    ...             discount = Decimal(0)
    ...         else:
    ...             discount = self.promotion(self)
    ...         return self.total() - discount
    ...     def __repr__(self):
    ...         return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'

    ... ...
    >>> def fidelity_promo(order: Order) -> Decimal:
    ...    if order.customer.fidelity >= 1000:
    ...        return order.total() * Decimal('0.05')
    ...    return Decimal(0)
    ... ...
    >>> def bulk_item_promo(order: Order) -> Decimal:
    ...    discount = Decimal(0)
    ...    for item in order.cart:
    ...        if item.quantity >= 20:
    ...            discount += item.total() * Decimal('0.1')
    ...    return discount
    ... ...
    >>> def large_order_promo(order: Order) -> Decimal:
    ...    distinct_items = {item.product for item in order.cart}
    ...    if len(distinct_items) >= 10:
    ...        return order.total() * Decimal('0.07')
    ...    return Decimal(0)
    >>> print("Start")
    >>> joe = Customer('John Doe', 0)
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 4, Decimal('.5')),
    ...         LineItem('apple', 10, Decimal('1.5')),
    ...         LineItem('watermelon', 5, Decimal(5))]
    >>> print(f"Joe -> cart -> fidelity_promo {Order(joe, cart, fidelity_promo)}")
    >>> print(f"Ann -> cart -> fidelity_promo {Order(ann, cart, fidelity_promo)}")
    >>> banana_cart = [LineItem('banana', 30, Decimal('.5')),
    ...                LineItem('apple', 10, Decimal('1.5'))]
    >>> print(f"Joe -> banana_cart -> bulk_item_promo {Order(joe, banana_cart, bulk_item_promo)}")
    >>> long_cart = [LineItem(str(item_code), 1, Decimal(1))
    ...               for item_code in range(10)]
    >>> print(f"Joe -> long_cart -> large_order_promo {Order(joe, long_cart, large_order_promo)}")
    >>> print(f"Joe -> cart -> large_order_promo {Order(joe, cart, large_order_promo)}")
    >>> print("Using best_promo function to select the discount")
    >>> promos = [fidelity_promo, bulk_item_promo, large_order_promo]
    >>> def best_promo(order: Order) -> Decimal:
    ...     return max(promo(order) for promo in promos)
    >>> print(f"Joe -> long_cart -> best_promo {Order(joe, long_cart, best_promo)}")
    >>> print(f"Joe -> banana_cart -> best_promo {Order(joe, banana_cart, best_promo)}")
    >>> print(f"Joe -> cart -> best_promo {Order(joe, cart, best_promo)}")
    ```

`Using the first-class functions approach reduces the runtime cost of instantiating the Order object every time`. When using classes, to avoid this issue, it is recommended to use another design pattern, such as the Flyweight pattern, which can make the code more complex.

## Decorator-Enhanced Strategy Pattern

## Command with First-Class Functions

## References

- [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
