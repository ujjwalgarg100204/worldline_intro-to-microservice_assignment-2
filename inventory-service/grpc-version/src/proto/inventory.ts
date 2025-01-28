import type * as grpc from '@grpc/grpc-js';
import type { MessageTypeDefinition } from '@grpc/proto-loader';

import type { InventoryServiceClient as _InventoryServiceClient, InventoryServiceDefinition as _InventoryServiceDefinition } from './InventoryService';

type SubtypeConstructor<Constructor extends new (...args: any) => any, Subtype> = {
  new(...args: ConstructorParameters<Constructor>): Subtype;
};

export interface ProtoGrpcType {
  CheckInventoryRequest: MessageTypeDefinition
  CheckInventoryResponse: MessageTypeDefinition
  InventoryService: SubtypeConstructor<typeof grpc.Client, _InventoryServiceClient> & { service: _InventoryServiceDefinition }
  UpdateInventoryRequest: MessageTypeDefinition
  UpdateInventoryResponse: MessageTypeDefinition
}

