from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float


class CreateOrderRequest(BaseModel):
    customer_id: str
    items: List[OrderItem]


class CreateOrderResponse(BaseModel):
    order_id: str


class GetOrderResponse(BaseModel):
    order_id: str
    status: str
    items: List[OrderItem]


class UpdateOrderStatusRequest(BaseModel):
    order_id: str
    new_status: str


class UpdateOrderStatusResponse(BaseModel):
    success: bool
