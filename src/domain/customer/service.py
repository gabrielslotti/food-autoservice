from adapters.db.schema import CustomerTable
from adapters.customer_adapter import CustomerAdapter

from pydantic import BaseModel, ConfigDict


class CustomerModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    cpf: str
    first_name: str
    last_name: str
    email: str

    @staticmethod
    def from_db_model(customer: CustomerTable):
        return CustomerModel.model_validate(customer)


class CustomerService:
    def __init__(self) -> None:
        self.customer_adapter = CustomerAdapter()

    def register(self, customer: CustomerModel) -> None:
        customer = CustomerTable(**customer.model_dump())
        self.customer_adapter.register(customer=customer)

    def get(self, cpf) -> CustomerModel:
        customer = self.customer_adapter.get(cpf=cpf)
        return CustomerModel.from_db_model(customer)
