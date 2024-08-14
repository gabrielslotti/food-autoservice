from typing import Protocol

from adapters.db.schema import CustomerTable


class CustomerPort(Protocol):

    def register(self, customer: CustomerTable) -> None:
        """Create a new customer row"""

    def get(self, customer_cpf: str) -> CustomerTable:
        """Get a single customer by cpf"""
