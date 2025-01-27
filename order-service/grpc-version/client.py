import grpc
from proto_generated import order_pb2, order_pb2_grpc


def run():
    # Connect to the gRPC server
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = order_pb2_grpc.OrderServiceStub(channel)

        # Create an order
        create_order_response = stub.CreateOrder(
            order_pb2.CreateOrderRequest(
                customerId="12345",
                items=[
                    order_pb2.OrderItem(productId="P001", quantity=2, price=10.5),
                    order_pb2.OrderItem(productId="P002", quantity=1, price=15.0),
                ],
            )
        )
        print(f"Order Created: {create_order_response.orderId}")

        # Get the order
        get_order_response = stub.GetOrder(
            order_pb2.GetOrderRequest(orderId=create_order_response.orderId)
        )
        print(f"Order Retrieved: {get_order_response}")

        # Update the order status
        update_status_response = stub.UpdateOrderStatus(
            order_pb2.UpdateOrderStatusRequest(
                orderId=create_order_response.orderId, newStatus="Shipped"
            )
        )
        print(f"Order Status Updated: {update_status_response.success}")


if __name__ == "__main__":
    run()
