# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import order_pb2 as order__pb2


class OrderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOrder = channel.unary_unary(
                '/OrderService/CreateOrder',
                request_serializer=order__pb2.CreateOrderRequest.SerializeToString,
                response_deserializer=order__pb2.CreateOrderResponse.FromString,
                )
        self.GetOrder = channel.unary_unary(
                '/OrderService/GetOrder',
                request_serializer=order__pb2.GetOrderRequest.SerializeToString,
                response_deserializer=order__pb2.GetOrderResponse.FromString,
                )
        self.UpdateOrderStatus = channel.unary_unary(
                '/OrderService/UpdateOrderStatus',
                request_serializer=order__pb2.UpdateOrderStatusRequest.SerializeToString,
                response_deserializer=order__pb2.UpdateOrderStatusResponse.FromString,
                )


class OrderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOrderStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrder,
                    request_deserializer=order__pb2.CreateOrderRequest.FromString,
                    response_serializer=order__pb2.CreateOrderResponse.SerializeToString,
            ),
            'GetOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrder,
                    request_deserializer=order__pb2.GetOrderRequest.FromString,
                    response_serializer=order__pb2.GetOrderResponse.SerializeToString,
            ),
            'UpdateOrderStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOrderStatus,
                    request_deserializer=order__pb2.UpdateOrderStatusRequest.FromString,
                    response_serializer=order__pb2.UpdateOrderStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OrderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/CreateOrder',
            order__pb2.CreateOrderRequest.SerializeToString,
            order__pb2.CreateOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/GetOrder',
            order__pb2.GetOrderRequest.SerializeToString,
            order__pb2.GetOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateOrderStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/OrderService/UpdateOrderStatus',
            order__pb2.UpdateOrderStatusRequest.SerializeToString,
            order__pb2.UpdateOrderStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
