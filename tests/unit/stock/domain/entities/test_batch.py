from datetime import date
from src.stock.domain.entities.batch import Batch
from src.stock.domain.value_objects.order_line import OrderLine


class TestBatch:
    def test_cant_allocate_a_order_from_a_different_product(self):
        order_line = OrderLine(order_id="ORD-0001", product_sku="SK-001", quantity=10)
        batch = Batch(
            reference="REF-00001", product_sku="SK-999", quantity=20, eta=date.today()
        )

        result = batch.can_allocate(order_line)

        assert not result

    def test_can_allocate_orders_when_are_from_same_product(self):
        order_line = OrderLine(order_id="ORD-0001", product_sku="SK-001", quantity=10)
        batch = Batch(
            reference="REF-00001", product_sku="SK-001", quantity=20, eta=date.today()
        )

        result = batch.can_allocate(order_line)

        assert result

    def test_cant_allocate_orders_from_other_products(self):
        order_line = OrderLine(order_id="ORD-0001", product_sku="SK-001", quantity=10)
        batch = Batch(
            reference="REF-00001", product_sku="SK-999", quantity=20, eta=date.today()
        )

        batch.allocate(order_line)

        assert not len(batch._allocations)

    def test_cant_allocate_if_stock_is_not_enough(self):
        order_line = OrderLine(order_id="ORD-0001", product_sku="SK-001", quantity=10)
        batch = Batch(
            reference="REF-00001", product_sku="SK-001", quantity=2, eta=date.today()
        )

        batch.allocate(order_line)

        assert not len(batch._allocations)

    def test_allocate_a_product_update_available_stock(self):
        order_line = OrderLine(order_id="ORD-0001", product_sku="SK-001", quantity=10)
        batch = Batch(
            reference="REF-00001", product_sku="SK-001", quantity=20, eta=date.today()
        )

        batch.allocate(order_line)

        assert (
            batch.available_quantity == batch._purchased_quantity - order_line.quantity
        )
