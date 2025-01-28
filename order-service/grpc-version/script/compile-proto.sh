#!/bin/bash

python -m grpc_tools.protoc \
  -I=proto \
  --pyi_out=. \
  --python_out=. \
  --grpc_python_out=. \
  proto/order.proto

echo "Proto files compiled to proto_generated directory successfully!"
