from typing import Protocol, List

from adapters.db.schema import OrderTable


class OrderPort(Protocol):

    def list(self) -> List[OrderTable]:
        """List all orders"""

    def checkout(self, order_id: int) -> None:
        """Chekout the order"""
