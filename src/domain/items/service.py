from adapters.db.schema import ItemsTable
from adapters.items_adapter import ItemsAdapter

from enum import Enum
from typing import List
from pydantic import BaseModel, ConfigDict


class CategoryEnum(str, Enum):
    lanche = 'Lanche'
    acompanhamento = 'Acompanhamento'
    bebida = 'Bebida'
    sobremesa = 'Sobremesa'


class ItemsModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None
    title: str
    description: str
    category: CategoryEnum
    amount: int
    price: float

    @staticmethod
    def from_db_model(item: ItemsTable):
        return ItemsModel.model_validate(item)


class ItemsService:
    def __init__(self) -> None:
        self.item_adapter = ItemsAdapter()

    def create(self, item: ItemsModel) -> None:
        category_id = self.item_adapter.get_category_id(item.category)

        item_to_create = item.model_dump()
        item_to_create['category'] = category_id

        item = ItemsTable(**item_to_create)
        self.item_adapter.create(item=item)

    def update(self, item: ItemsModel) -> None:
        item = ItemsTable(**item.model_dump())
        self.item_adapter.update(item=item)

    def delete(self, item_id: int) -> None:
        self.item_adapter.delete(item_id=item_id)

    def get_all_by_category(self, category: str) -> List[ItemsModel]:
        items = self.item_adapter.get_all_by_category(category=category)
        return [ItemsModel.from_db_model(item) for item in items]
