import express from "express";
import inventoryRoutes from "./routes/inventory.routes";

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Routes
app.use("/api/inventory", inventoryRoutes);

// Start the server
app.listen(PORT, () => {
  console.log(`Inventory REST API is running on http://localhost:${PORT}`);
});
