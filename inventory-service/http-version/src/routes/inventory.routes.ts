import { Router } from "express";
import {
  checkInventory,
  updateInventory,
} from "../controllers/inventory.controller";

const router = Router();

// Check inventory
router.post("/check", checkInventory);

// Update inventory
router.post("/update", updateInventory);

export default router;
