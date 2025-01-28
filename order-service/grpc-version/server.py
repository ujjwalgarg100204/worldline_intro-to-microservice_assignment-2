from concurrent import futures

import grpc

from logger import logger
from order_service import OrderService
import order_pb2_grpc


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=12))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    logger.info("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
