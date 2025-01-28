export interface CheckInventoryRequest {
  productId: string;
  quantity: number;
}

export interface CheckInventoryResponse {
  available: boolean;
}

export interface UpdateInventoryRequest {
  productId: string;
  quantity: number; // Positive for increase, negative for decrease
}

export interface UpdateInventoryResponse {
  success: boolean;
  updatedQuantity: number;
}
