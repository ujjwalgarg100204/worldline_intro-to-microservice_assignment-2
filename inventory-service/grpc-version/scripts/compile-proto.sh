#!/bin/bash

# Generate JavaScript code
# bun grpc_tools_node_protoc \
#   --js_out=import_style=commonjs:src/proto \
#   --ts_out=src/proto \
#   --grpc_out=grpc_js:src/proto \
#   -I=./proto \
#   ./proto/*.proto

./node_modules/.bin/proto-loader-gen-types --longs=String \
  --enums=String \
  --defaults \
  --oneofs \
  --grpcLib=@grpc/grpc-js \
  --outDir=src/proto/ \
  ./src/proto/*.proto
