import uuid
from typing import Dict
from models import CreateOrderRequest, GetOrderResponse

# In-memory database for orders
orders_db: Dict[str, Dict] = {
    "44de4ac1-a058-4f94-aa35-9ebfbfc429d7": {
        "status": "Pending",
        "items": ["item1", "item2"],
    },
    "192d589d-b98e-496b-acea-5314fff02e7a": {
        "status": "Shipped",
        "items": ["item3", "item4"],
    },
    "f68c403e-3beb-4bc4-a2a4-32a48225a054": {
        "status": "Delivered",
        "items": ["item5", "item6"],
    },
}


def create_order(order_data: CreateOrderRequest) -> str:
    order_id = str(uuid.uuid4())
    orders_db[order_id] = {
        "customer_id": order_data.customer_id,
        "status": "placed",
        "items": [item.model_dump() for item in order_data.items],
    }
    return order_id


def get_order(order_id: str) -> GetOrderResponse | None:
    order = orders_db.get(order_id)
    if not order:
        return None
    return GetOrderResponse(
        order_id=order_id,
        status=order["status"],
        items=order["items"],
    )


def update_order_status(order_id: str, new_status: str) -> bool:
    if order_id not in orders_db:
        return False
    orders_db[order_id]["status"] = new_status
    return True
