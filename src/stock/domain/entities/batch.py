from typing import Set
from datetime import date
from ..value_objects.order_line import OrderLine


class Batch:
    def __init__(
        self, reference: str, product_sku: str, quantity: int, eta: date | None
    ):
        self.reference = reference
        self.product_sku = product_sku
        self._purchased_quantity = quantity
        self.eta = eta
        self._allocations: Set[OrderLine] = set()

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __repr__(self):
        return f"<Batch {self.reference}>"

    def __gt__(self, other):
        if not self.eta:
            return False
        if not other.eta:
            return False
        return self.eta > other.eta

    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine) -> None:
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(order_line.quantity for order_line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return (
            self.product_sku == line.product_sku
            and self.available_quantity >= line.quantity
        )
