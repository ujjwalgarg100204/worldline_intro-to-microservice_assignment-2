#!/bin/bash

python -m grpc_tools.protoc -I=proto --python_out=proto_generated --grpc_python_out=proto_generated proto/order.proto
echo "Proto files compiled to proto_generated directory successfully!"
