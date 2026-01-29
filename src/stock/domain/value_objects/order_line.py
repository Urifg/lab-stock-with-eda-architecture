from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    order_id: str
    product_sku: str
    quantity: int
