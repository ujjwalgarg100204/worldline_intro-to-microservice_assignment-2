import uuid

from proto_generated import order_pb2, order_pb2_grpc


class OrderService(order_pb2_grpc.OrderServiceServicer):
    def __init__(self):
        # In-memory storage for orders
        self.orders = {}

    def CreateOrder(self, request, context):
        # Generate a unique order ID
        order_id = str(uuid.uuid4())
        # Save the order
        self.orders[order_id] = {
            "status": "Pending",
            "items": request.items,
        }
        # Return the response
        return order_pb2.CreateOrderResponse(orderId=order_id)

    def GetOrder(self, request, context):
        # Retrieve the order
        order = self.orders.get(request.orderId)
        if not order:
            context.abort(grpc.StatusCode.NOT_FOUND, "Order not found")
        return order_pb2.GetOrderResponse(
            orderId=request.orderId,
            status=order["status"],
            items=order["items"],
        )

    def UpdateOrderStatus(self, request, context):
        # Check if the order exists
        order = self.orders.get(request.orderId)
        if not order:
            context.abort(grpc.StatusCode.NOT_FOUND, "Order not found")
        # Update the status
        order["status"] = request.newStatus
        return order_pb2.UpdateOrderStatusResponse(success=True)
