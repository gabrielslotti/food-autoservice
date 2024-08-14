from typing import Protocol, List

from adapters.db.schema import ItemsTable


class ItemsPort(Protocol):

    def create(self, item: ItemsTable) -> None:
        """Create a new item"""

    def update(self, item: ItemsTable) -> None:
        """Update a single item"""

    def remove(self, id_item: int) -> None:
        """Remove a single item"""

    def get_by_category(self, category: str) -> List[ItemsTable]:
        """Get items by category"""
