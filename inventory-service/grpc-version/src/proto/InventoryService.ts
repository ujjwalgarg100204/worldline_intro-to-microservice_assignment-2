// Original file: proto/inventory.proto

import type * as grpc from '@grpc/grpc-js'
import type { MethodDefinition } from '@grpc/proto-loader'
import type { CheckInventoryRequest as _CheckInventoryRequest, CheckInventoryRequest__Output as _CheckInventoryRequest__Output } from './CheckInventoryRequest';
import type { CheckInventoryResponse as _CheckInventoryResponse, CheckInventoryResponse__Output as _CheckInventoryResponse__Output } from './CheckInventoryResponse';
import type { UpdateInventoryRequest as _UpdateInventoryRequest, UpdateInventoryRequest__Output as _UpdateInventoryRequest__Output } from './UpdateInventoryRequest';
import type { UpdateInventoryResponse as _UpdateInventoryResponse, UpdateInventoryResponse__Output as _UpdateInventoryResponse__Output } from './UpdateInventoryResponse';

export interface InventoryServiceClient extends grpc.Client {
  CheckInventory(argument: _CheckInventoryRequest, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_CheckInventoryResponse__Output>): grpc.ClientUnaryCall;
  CheckInventory(argument: _CheckInventoryRequest, metadata: grpc.Metadata, callback: grpc.requestCallback<_CheckInventoryResponse__Output>): grpc.ClientUnaryCall;
  CheckInventory(argument: _CheckInventoryRequest, options: grpc.CallOptions, callback: grpc.requestCallback<_CheckInventoryResponse__Output>): grpc.ClientUnaryCall;
  CheckInventory(argument: _CheckInventoryRequest, callback: grpc.requestCallback<_CheckInventoryResponse__Output>): grpc.ClientUnaryCall;
  checkInventory(argument: _CheckInventoryRequest, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_CheckInventoryResponse__Output>): grpc.ClientUnaryCall;
  checkInventory(argument: _CheckInventoryRequest, metadata: grpc.Metadata, callback: grpc.requestCallback<_CheckInventoryResponse__Output>): grpc.ClientUnaryCall;
  checkInventory(argument: _CheckInventoryRequest, options: grpc.CallOptions, callback: grpc.requestCallback<_CheckInventoryResponse__Output>): grpc.ClientUnaryCall;
  checkInventory(argument: _CheckInventoryRequest, callback: grpc.requestCallback<_CheckInventoryResponse__Output>): grpc.ClientUnaryCall;
  
  UpdateInventory(argument: _UpdateInventoryRequest, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_UpdateInventoryResponse__Output>): grpc.ClientUnaryCall;
  UpdateInventory(argument: _UpdateInventoryRequest, metadata: grpc.Metadata, callback: grpc.requestCallback<_UpdateInventoryResponse__Output>): grpc.ClientUnaryCall;
  UpdateInventory(argument: _UpdateInventoryRequest, options: grpc.CallOptions, callback: grpc.requestCallback<_UpdateInventoryResponse__Output>): grpc.ClientUnaryCall;
  UpdateInventory(argument: _UpdateInventoryRequest, callback: grpc.requestCallback<_UpdateInventoryResponse__Output>): grpc.ClientUnaryCall;
  updateInventory(argument: _UpdateInventoryRequest, metadata: grpc.Metadata, options: grpc.CallOptions, callback: grpc.requestCallback<_UpdateInventoryResponse__Output>): grpc.ClientUnaryCall;
  updateInventory(argument: _UpdateInventoryRequest, metadata: grpc.Metadata, callback: grpc.requestCallback<_UpdateInventoryResponse__Output>): grpc.ClientUnaryCall;
  updateInventory(argument: _UpdateInventoryRequest, options: grpc.CallOptions, callback: grpc.requestCallback<_UpdateInventoryResponse__Output>): grpc.ClientUnaryCall;
  updateInventory(argument: _UpdateInventoryRequest, callback: grpc.requestCallback<_UpdateInventoryResponse__Output>): grpc.ClientUnaryCall;
  
}

export interface InventoryServiceHandlers extends grpc.UntypedServiceImplementation {
  CheckInventory: grpc.handleUnaryCall<_CheckInventoryRequest__Output, _CheckInventoryResponse>;
  
  UpdateInventory: grpc.handleUnaryCall<_UpdateInventoryRequest__Output, _UpdateInventoryResponse>;
  
}

export interface InventoryServiceDefinition extends grpc.ServiceDefinition {
  CheckInventory: MethodDefinition<_CheckInventoryRequest, _CheckInventoryResponse, _CheckInventoryRequest__Output, _CheckInventoryResponse__Output>
  UpdateInventory: MethodDefinition<_UpdateInventoryRequest, _UpdateInventoryResponse, _UpdateInventoryRequest__Output, _UpdateInventoryResponse__Output>
}
