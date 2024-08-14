from fastapi import APIRouter
from domain.items.service import ItemsService, ItemsModel, CategoryEnum

router = APIRouter()
items_service = ItemsService()


@router.post('/create')
def create_item(item: ItemsModel):
    """Create a new menu item.

    Returns:
        dict: A dictionary containing a message that the item had been created.
    """

    items_service.create(item=ItemsModel(**item.model_dump()))
    return {'message': f'item {item.title} created'}


@router.put('/update')
def update_item(item: ItemsModel):
    """Update an menu item.

    Returns:
        dict: A dictionary containing a message that the item had been updated.
    """

    items_service.update(item=ItemsModel(**item.model_dump()))
    return {'message': f'item {item.title} updated'}


@router.delete('/delete/{item_id}')
def delete_item(item_id: int):
    """Delete a menu item by its ID.

    Args:
        item_id (int): The ID of the item to delete.
    Returns:
        dict: A dictionary containing a message that the item had been deleted.
    """

    items_service.delete(item_id=item_id)
    return {'message': 'item deleted'}


@router.get('/list/{category}')
def list_item_by_category(category: CategoryEnum):
    """Retrieve a list with all items in a given category.

    Args:
        category (str): The category of a group of items.
    Returns:
        list: A list of dictionary where each dictionary
              corresponds to an item.
    """

    return items_service.get_all_by_category(category=category)
