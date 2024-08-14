from fastapi import APIRouter
from domain.customer.service import CustomerService, CustomerModel

router = APIRouter()
customer_service = CustomerService()


@router.post('/register')
def register_customer(customer: CustomerModel):
    """Register a new customer.

    Returns:
        dict: An dictionary containing a message informing that the customer
              had been registered.
    """
    customer_service.register(customer=CustomerModel(**customer.model_dump()))
    return {'message': f'customer {customer.cpf} registered'}


@router.get('/identify/{cpf}')
def identify_customer(cpf: str):
    """Identifies a customer by its CPF.

    Args:
        cpf (str): The CPF of the customer to retrieve.
    Returns:
        dict: An dictionary containing customer info.
    """
    return customer_service.get(cpf=cpf)
