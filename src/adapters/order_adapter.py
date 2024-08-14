from adapters.db.schema import OrderTable, OrderStatusTable, DBSession
from domain.ports.order import OrderPort


class OrderAdapter(OrderPort):
    def __init__(self) -> None:
        self.db_session = DBSession()

    def list(self) -> OrderTable:
        with self.db_session.get_db() as db:
            return db.query(OrderTable)\
                    .with_entities(
                        OrderTable.id,
                        OrderTable.customer_id,
                        OrderTable.items,
                        OrderStatusTable.description.label('status')
                    )\
                    .join(OrderStatusTable)\
                    .all()

    def checkout(self, order_id: int) -> None:
        with self.db_session.get_db() as db:
            # Get status Finalizado
            finished_order_status = db.query(OrderStatusTable)\
                                      .filter(OrderStatusTable.description == 'Finalizado')\
                                      .one_or_none()

            # Get the given order
            order = db.query(OrderTable)\
                      .filter(OrderTable.id == order_id)\
                      .one_or_none()

            # Update order status to Finalizado
            order.status = finished_order_status.id

            db.add(order)
            db.commit()
