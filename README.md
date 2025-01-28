# Project: E-commerce Order Management System

This project is submitted as Assignment-2 for course "Introduction to Microservices"
under worldline training. This project tries to showcase microservices using
multiple programming each using their own framework and communicating using
gRPC instead of JSON

## Details of Microservices

### 1. Inventory Service

- Programming Language: TypeScript with Bun.js (express for REST)
- **Responsibilities:**
  - **Check product availability:** Determine if a specific quantity of a product
    is available.
  - **Update inventory levels:** Increase or decrease inventory levels based on orders.
- **Endpoints:**
  - **HTTP:**
    - `/inventory/check/{productId}/{quantity}` (GET)
    - `/inventory/update/{productId}/{quantity}` (POST/PUT)
  - **gRPC:**
    - `CheckInventory` (Unary) - Request: productId, quantity; Response: boolean
      (available/unavailable)
    - `UpdateInventory` (Unary) - Request: productId, quantity
      (positive for increase, negative for decrease); Response:
      InventoryUpdateResponse (success/failure, updated quantity)

### 2. Order Service

- Programming Language: Python (FastAPI for REST)
- **Responsibilities:**
  - **Create orders:** Receive order details from the frontend and initiate the
    order creation process.
  - **Manage order status:** Update order status (e.g., placed, shipped,
    delivered, canceled).
  - **Orchestrate interactions:** Coordinate interactions with Inventory and
    Shipping services.
- **Endpoints:**
  - **HTTP:**
    - `/orders` (POST) - Create an order
    - `/orders/{orderId}` (GET) - Retrieve order details
    - `/orders/{orderId}/status` (PUT) - Update order status
  - **gRPC:**
    - `CreateOrder` (Unary) - Request: Order details; Response: OrderId
    - `GetOrder` (Unary) - Request: OrderId; Response: OrderDetails
    - `UpdateOrderStatus` (Unary) - Request: OrderId, newStatus; Response:
      OrderStatusUpdateResponse (success/failure)

### 3. Shipping Service

- Programming Language: Java (Spring for both)
- **Responsibilities:**
  - **Calculate shipping costs:** Determine shipping costs based on destination and
    delivery options.
  - **Schedule deliveries:** Coordinate with shipping carriers to schedule deliveries.
  - **Track shipments:** Provide real-time shipment tracking information.
- **Endpoints:**
  - **HTTP:**
    - `/shipping/cost` (POST) - Calculate shipping cost for an order
    - `/shipping/schedule` (POST) - Schedule a delivery
    - `/shipping/track/{trackingId}` (GET) - Get shipment tracking information
  - **gRPC:**
    - `CalculateShippingCost` (Unary) - Request: Order details (destination,
      weight, etc.); Response: ShippingCost
    - `ScheduleDelivery` (Unary) - Request: OrderId, shippingMethod;
      Response: DeliverySchedule
    - `TrackShipment` (Unary) - Request: TrackingId; Response: ShipmentTrackingInfo

## Trying out each Microservice on your own machine

All commands assume that you are in root of the project and written from that
perspective

### 1. Inventory Service

#### gRPC Version

1. Requirement: bun
2. Install all dependencies

   ```bash
   cd ./inventory-service/grpc-version/
   bun install
   ```

3. To generate typescript types from proto file run

   ```bash
   cd ./inventory-service/grpc-version/
   ./scripts/compile-proto.sh
   ```

   TS files will be generated in proto directory

4. To run the microservice

   ```bash
   cd ./inventory-service/grpc-version/
   bun run start
   ```

#### REST Version

1. Requirement: bun
2. Install all dependencies

   ```bash
   cd ./inventory-service/http-version/
   bun install
   ```

3. To run the microservice

   ```bash
   cd ./inventory-service/http-version/
   bun run start
   ```

### 2. Order Service

Requirement:

- Python 3.12
- Anaconda or Miniconda

#### gRPC Version

1. Create conda environment from `env.yml`

   ```bash
   cd ./order-service/grpc-version/
   conda env create --file env.yml
   ```

2. Activate that environment

   ```bash
   conda activate microsvc__order_management_sys__order_sys
   ```

3. If you need you can re-compile proto file and generate python files by using
   following command

   ```bash
   cd ./order-service/grpc-version/
   ./script/compile-proto.sh
   ```

4. Run the project

   ```bash
   cd ./order-service/grpc-version/
   python3 server.py
   ```

#### REST Version

1. Create and activate conda environment just like gRPC version
2. Run the project

   ```bash
   cd ./order-service/grpc-version/
   fastapi run app.py
   ```

### 3. Shipping Service

Requirement:

- Java 17

#### gRPC Version

1. Run the project

   ```bash
   cd ./shipping-service/grpc-version/
   ./mvnw clean install compile spring-boot:run
   ```

#### REST Version

1. Run the project

   ```bash
   cd ./shipping-service/http-version/
   ./mvnw clean install compile spring-boot:run
   ```
