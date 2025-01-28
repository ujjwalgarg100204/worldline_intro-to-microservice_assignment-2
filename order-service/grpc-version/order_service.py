import uuid

import grpc
import order_pb2
import order_pb2_grpc
from logger import logger


class OrderService(order_pb2_grpc.OrderServiceServicer):
    def __init__(self):
        # In-memory storage for orders
        self.orders: dict[str, dict] = {
            "44de4ac1-a058-4f94-aa35-9ebfbfc429d7": {
                "status": "Pending",
                "items": [
                    order_pb2.OrderItem(
                        product_id="product-1", quantity=2, price=19.99
                    ),
                    order_pb2.OrderItem(product_id="product-2", quantity=1, price=9.99),
                ],
            },
            "192d589d-b98e-496b-acea-5314fff02e7a": {
                "status": "Shipped",
                "items": [
                    order_pb2.OrderItem(
                        product_id="product-3", quantity=3, price=29.99
                    ),
                    order_pb2.OrderItem(
                        product_id="product-4", quantity=2, price=14.99
                    ),
                ],
            },
            "f68c403e-3beb-4bc4-a2a4-32a48225a054": {
                "status": "Delivered",
                "items": [
                    order_pb2.OrderItem(
                        product_id="product-5", quantity=1, price=49.99
                    ),
                    order_pb2.OrderItem(product_id="product-6", quantity=4, price=7.99),
                ],
            },
        }
        logger.info("OrderService initialized with an empty order store.")

    def CreateOrder(self, request, context):
        logger.info("Received CreateOrder request with items: %s", request.items)

        # Generate a unique order ID
        order_id = str(uuid.uuid4())

        # Save the order
        self.orders[order_id] = {
            "status": "Pending",
            "items": request.items,
        }
        logger.info(
            "Order created with ID: %s, Status: Pending, Items: %s",
            order_id,
            request.items,
        )

        # Return the response
        return order_pb2.CreateOrderResponse(order_id=order_id)

    def GetOrder(self, request, context):
        logger.info("Received GetOrder request for order ID: %s", request.order_id)

        # Retrieve the order
        order = self.orders.get(request.order_id)
        if not order:
            logger.error("Order with ID %s not found.", request.order_id)
            context.abort(grpc.StatusCode.NOT_FOUND, "Order not found")

        logger.info(
            "Order retrieved: ID: %s, Status: %s, Items: %s",
            request.order_id,
            order["status"],
            order["items"],
        )
        return order_pb2.GetOrderResponse(
            order_id=request.order_id,
            status=order["status"],
            items=order["items"],
        )

    def UpdateOrderStatus(self, request, context):
        logger.info(
            "Received UpdateOrderStatus request for order ID: %s, New Status: %s",
            request.order_id,
            request.new_status,
        )

        # Check if the order exists
        order = self.orders.get(request.order_id)
        if not order:
            logger.error(
                "Order with ID %s not found for status update.", request.order_id
            )
            context.abort(grpc.StatusCode.NOT_FOUND, "Order not found")

        # Update the status
        old_status = order["status"]
        order["status"] = request.new_status
        logger.info(
            "Order status updated for ID: %s, Old Status: %s, New Status: %s",
            request.order_id,
            old_status,
            request.new_status,
        )

        return order_pb2.UpdateOrderStatusResponse(success=True)
