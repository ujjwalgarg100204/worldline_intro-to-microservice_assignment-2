import grpc
from fastapi import FastAPI
from grpc_fastapi.reflect import GRPCReflection
from grpc_fastapi.route import grpc_route
from concurrent import futures

from proto_generated import order_pb2_grpc
from order_service import OrderService

app = FastAPI()

# Initialize the gRPC server
grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# Add the OrderService to the gRPC server
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), grpc_server)

# Add reflection for gRPC service discovery
reflection = GRPCReflection(grpc_server)

# Add the gRPC route to FastAPI
app.add_route("/grpc", grpc_route(grpc_server, reflection))
