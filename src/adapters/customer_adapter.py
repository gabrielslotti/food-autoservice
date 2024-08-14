from adapters.db.schema import CustomerTable, DBSession
from domain.ports.customer import CustomerPort


class CustomerAdapter(CustomerPort):
    def __init__(self) -> None:
        self.db_session = DBSession()

    def register(self, customer: CustomerTable) -> None:
        with self.db_session.get_db() as db:
            db.add(customer)
            db.commit()

    def get(self, cpf: str) -> CustomerTable:
        with self.db_session.get_db() as db:
            return db.query(CustomerTable)\
                    .filter(CustomerTable.cpf == cpf)\
                    .one_or_none()
