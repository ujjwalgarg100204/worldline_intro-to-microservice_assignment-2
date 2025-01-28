import type { Request, Response } from "express";
import type {
  CheckInventoryRequest,
  CheckInventoryResponse,
  UpdateInventoryRequest,
  UpdateInventoryResponse,
} from "../types/inventory.types";
import logger from "../logger";

// Mock inventory data
const inventory: Record<string, number> = {
  "product-1": 100,
  "product-2": 50,
  "product-3": 0,
};

// Check inventory
export const checkInventory = (
  req: Request<{}, CheckInventoryResponse, CheckInventoryRequest>,
  res: Response<CheckInventoryResponse>,
) => {
  const { productId, quantity } = req.body;

  // Validate request
  if (!productId || quantity === undefined) {
    logger.warn(`Invalid request: ${JSON.stringify(req.body)}`);
    res.status(400).json({ available: false });
    return;
  }

  // Check if product exists
  const availableQuantity = inventory[productId];
  if (availableQuantity === undefined) {
    logger.warn(`Product not found: ${productId}`);
    res.status(404).json({ available: false });
    return;
  }

  // Check if enough quantity is available
  const response = {
    available: availableQuantity >= quantity,
  } satisfies CheckInventoryResponse;

  logger.info(
    `Inventory checked for product ${productId}: ${JSON.stringify(response)}`,
  );
  res.json(response);
};

// Update inventory
export const updateInventory = (
  req: Request<{}, UpdateInventoryResponse, UpdateInventoryRequest>,
  res: Response<UpdateInventoryResponse>,
) => {
  const { productId, quantity } = req.body;

  // Validate request
  if (!productId || quantity === undefined) {
    logger.warn(`Invalid request: ${JSON.stringify(req.body)}`);
    res.status(400).json({ success: false, updatedQuantity: 0 });
    return;
  }

  // Check if product exists
  if (!inventory[productId]) {
    logger.warn(`Product not found: ${productId}`);
    res.status(404).json({ success: false, updatedQuantity: 0 });
    return;
  }

  // Update inventory (increase or decrease)
  inventory[productId] += quantity;

  // Ensure inventory doesn't go below 0
  if (inventory[productId] < 0) {
    inventory[productId] = 0;
  }

  const response = {
    success: true,
    updatedQuantity: inventory[productId],
  } satisfies UpdateInventoryResponse;

  logger.info(
    `Inventory updated for product ${productId}: ${JSON.stringify(response)}`,
  );
  res.json(response);
};
