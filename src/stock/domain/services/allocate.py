from ..entities.batch import Batch
from ..value_objects.order_line import OrderLine
from ..exceptions.out_of_stock import OutOfStockException


def allocate(order_line: OrderLine, batches: list[Batch]) -> str:
    try:
        batch: Batch = next(b for b in sorted(batches) if b.can_allocate(order_line))
        batch.allocate(order_line)
        return batch.reference
    except StopIteration:
        raise OutOfStockException(f"Out of stock for sku {order_line.product_sku}")
