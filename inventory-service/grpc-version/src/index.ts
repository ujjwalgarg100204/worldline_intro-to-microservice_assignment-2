import * as grpc from "@grpc/grpc-js";
import * as protoLoader from "@grpc/proto-loader";
import path from "path";
import logger from "./logger";
import type { ProtoGrpcType } from "./proto/inventory";
import InventoryService from "./service/inventory-service";

const protoPath = path.join(__dirname, "proto", "inventory.proto");
const packageDefinition = protoLoader.loadSync(protoPath, {
  enums: String,
  defaults: true,
  oneofs: true,
});
const proto = grpc.loadPackageDefinition(
  packageDefinition,
) as unknown as ProtoGrpcType;

const server = new grpc.Server();

const inventoryService = new InventoryService();
server.addService(proto.InventoryService.service, {
  checkInventory: inventoryService.checkInventory.bind(inventoryService),
  updateInventory: inventoryService.updateInventory.bind(inventoryService),
});

const PORT = process.env.PORT || 50051;
server.bindAsync(
  `0.0.0.0:${PORT}`,
  grpc.ServerCredentials.createInsecure(),
  (error, port) => {
    if (error) {
      logger.error(`Server error: ${error}`);
      console.error(`Server error: ${error}`);
    } else {
      logger.info(`Server is running on port: ${port}`);
    }
  },
);
