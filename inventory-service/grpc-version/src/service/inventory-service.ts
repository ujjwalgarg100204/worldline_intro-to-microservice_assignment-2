import * as grpc from "@grpc/grpc-js";
import logger from "../logger";
import type { CheckInventoryRequest } from "../proto/CheckInventoryRequest";
import type { CheckInventoryResponse } from "../proto/CheckInventoryResponse";
import type { UpdateInventoryRequest } from "../proto/UpdateInventoryRequest";
import type { UpdateInventoryResponse } from "../proto/UpdateInventoryResponse";

class InventoryService {
  private inventory: { [key: string]: number } = {};

  checkInventory(
    call: grpc.ServerUnaryCall<CheckInventoryRequest, CheckInventoryResponse>,
    callback: grpc.sendUnaryData<CheckInventoryResponse>,
  ): void {
    const { productId, quantity } = call.request;
    logger.info(JSON.stringify({ productId, quantity }));
    if (!productId) {
      return callback(
        {
          code: grpc.status.INVALID_ARGUMENT,
          message: "Product ID is required",
        },
        null,
      );
    }
    if (!quantity) {
      return callback(
        { code: grpc.status.INVALID_ARGUMENT, message: "Quantity is required" },
        null,
      );
    }
    const available = (this.inventory[productId] || 0) >= quantity;

    const response = { available: available } satisfies CheckInventoryResponse;

    logger.info(
      `Checked inventory for productId: ${productId}, quantity: ${quantity}, available: ${available}`,
    );

    callback(null, response);
  }

  updateInventory(
    call: grpc.ServerUnaryCall<UpdateInventoryRequest, UpdateInventoryResponse>,
    callback: grpc.sendUnaryData<UpdateInventoryResponse>,
  ): void {
    const { productId, quantity } = call.request;
    logger.info(JSON.stringify({ productId, quantity }));
    logger.info(JSON.stringify(call.request));
    if (!productId) {
      return callback(
        {
          code: grpc.status.INVALID_ARGUMENT,
          message: "Product ID is required",
        },
        null,
      );
    }
    if (!quantity) {
      return callback(
        { code: grpc.status.INVALID_ARGUMENT, message: "Quantity is required" },
        null,
      );
    }
    const currentQuantity = this.inventory[productId] || 0;
    const updatedQuantity = currentQuantity + quantity;

    this.inventory[productId] = updatedQuantity;

    const response = {
      success: true,
      updatedQuantity: updatedQuantity,
    } satisfies UpdateInventoryResponse;

    logger.info(
      `Updated inventory for productId: ${productId}, quantity: ${quantity}, updatedQuantity: ${updatedQuantity}`,
    );

    callback(null, response);
  }
}

export default InventoryService;
