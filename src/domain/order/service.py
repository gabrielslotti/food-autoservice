from adapters.db.schema import OrderTable
from adapters.order_adapter import OrderAdapter

from enum import Enum
from pydantic import BaseModel, ConfigDict


class StatusEnum(str, Enum):
    recebido = 'Recebido'
    em_preparacao = 'Em preparação'
    pronto = 'Pronto'
    finalizado = 'Finalizado'


class OrderModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None
    customer_id: int | None
    status: StatusEnum
    items: dict

    @staticmethod
    def from_db_model(order: OrderTable):
        return OrderModel.model_validate(order)


class OrderService:
    def __init__(self) -> None:
        self.order_adapter = OrderAdapter()

    def list(self) -> OrderModel:
        orders = self.order_adapter.list()
        return [OrderModel.from_db_model(order) for order in orders]

    def checkout(self, order_id: int) -> None:
        return self.order_adapter.checkout(order_id=order_id)
