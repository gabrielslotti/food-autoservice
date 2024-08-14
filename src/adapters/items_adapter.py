from adapters.db.schema import ItemsTable, ItemsCategoryTable, DBSession
from domain.ports.items import ItemsPort


class ItemsAdapter(ItemsPort):
    def __init__(self) -> None:
        self.db_session = DBSession()

    def create(self, item: ItemsTable) -> None:
        with self.db_session.get_db() as db:
            db.add(item)
            db.commit()

    def update(self, item: ItemsTable) -> None:
        with self.db_session.get_db() as db:
            item_to_update = db.query(ItemsTable)\
                    .filter(ItemsTable.id == item.id)\
                    .one_or_none()

            if item_to_update is None:
                raise ValueError("Error: Item not found")

            item_to_update.title = item.title
            item_to_update.description = item.description
            item_to_update.amount = item.amount
            item_to_update.price = item.price

            db.add(item_to_update)
            db.commit()

    def delete(self, item_id: int) -> None:
        with self.db_session.get_db() as db:
            item = db.query(ItemsTable)\
                    .filter(ItemsTable.id == item_id)\
                    .one_or_none()

            db.delete(item)
            db.commit()

    def get_all_by_category(self, category: str) -> ItemsTable:
        with self.db_session.get_db() as db:
            return db.query(ItemsTable)\
                    .with_entities(
                        ItemsTable.id,
                        ItemsTable.title,
                        ItemsTable.description,
                        ItemsTable.amount,
                        ItemsTable.price,
                        ItemsCategoryTable.description.label('category')
                    )\
                    .join(ItemsCategoryTable)\
                    .filter(ItemsCategoryTable.description == category)\
                    .all()

    def get_category_id(self, category: str) -> int:
        with self.db_session.get_db() as db:
            category = db.query(ItemsCategoryTable)\
                    .filter(ItemsCategoryTable.description == category)\
                    .one_or_none()

            return category.id
