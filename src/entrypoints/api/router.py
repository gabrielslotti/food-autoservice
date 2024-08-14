from fastapi import APIRouter
from .customer import router as customer
from .items import router as items
from .order import router as order

router = APIRouter(prefix='/v1')

router.include_router(customer.router, prefix='/customer', tags=['customer'])
router.include_router(items.router, prefix='/items', tags=['items'])
router.include_router(order.router, prefix='/order', tags=['order'])
