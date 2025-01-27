from fastapi import FastAPI, HTTPException
from models import (
    CreateOrderRequest,
    CreateOrderResponse,
    GetOrderResponse,
    UpdateOrderStatusRequest,
    UpdateOrderStatusResponse,
)
from orders import create_order, get_order, update_order_status

app = FastAPI(title="Order Service HTTP", version="1.0")


@app.post("/orders", response_model=CreateOrderResponse)
async def create_order_endpoint(order_request: CreateOrderRequest):
    order_id = create_order(order_request)
    return {"order_id": order_id}


@app.get("/orders/{order_id}", response_model=GetOrderResponse)
async def get_order_endpoint(order_id: str):
    order = get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.put("/orders/{order_id}/status", response_model=UpdateOrderStatusResponse)
async def update_order_status_endpoint(
    order_id: str, status_request: UpdateOrderStatusRequest
):
    success = update_order_status(order_id, status_request.new_status)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"success": success}
