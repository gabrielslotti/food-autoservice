from fastapi import APIRouter
from domain.order.service import OrderService, OrderModel

from typing import List, Dict

router = APIRouter()
order_service = OrderService()


@router.get('/list')
def list_orders() -> List[OrderModel]:
    """List all orders created"""
    return order_service.list()


@router.get('/fake_checkout/{order_id}')
def fake_checkout(order_id: str) -> Dict[str, str]:
    """Fake checkout, only change the order status to 'Finalizado'.

    Args:
        order_id (int): The ID of the order to finish.
    Returns:
        dict: A dictionary containing a message that the order had been finished.
    """

    order_service.checkout(order_id=order_id)
    return {"message": f"order {order_id} finished"}
