package com.ujjwalgarg.order_management_sys.grpc_version.service;

import com.ujjwalgarg.order_management_sys.grpc_version.ShippingProto;
import com.ujjwalgarg.order_management_sys.grpc_version.ShippingProto.ShippingCostResponse;
import com.ujjwalgarg.order_management_sys.grpc_version.ShippingServiceGrpc;
import com.ujjwalgarg.order_management_sys.grpc_version.db.ScheduledDeliveriesManager;
import com.ujjwalgarg.order_management_sys.grpc_version.db.TrackingInfoManager;
import com.ujjwalgarg.order_management_sys.grpc_version.entity.DeliverySchedule;
import com.ujjwalgarg.order_management_sys.grpc_version.entity.ShipmentTrackingInfo;
import io.grpc.stub.StreamObserver;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class ShippingServiceImpl extends ShippingServiceGrpc.ShippingServiceImplBase {
  private final ScheduledDeliveriesManager deliveriesManager;
  private final TrackingInfoManager trackingInfoManager;

  @Override
  public void calculateShippingCost(
      ShippingProto.ShippingCostRequest request,
      StreamObserver<ShippingCostResponse> responseObserver) {
    log.info("Received calculateShippingCost request: {}", request);
    float baseRate = request.getShippingMethod().equalsIgnoreCase("express") ? 10 : 5;
    float cost = baseRate * request.getWeight();
    log.info("Calculated shipping cost: {}", cost);

    ShippingProto.ShippingCostResponse response =
        ShippingProto.ShippingCostResponse.newBuilder().setSuccess(true).setCost(cost).build();
    responseObserver.onNext(response);
    responseObserver.onCompleted();
    log.info("Sent calculateShippingCost response: {}", response);
  }

  @Override
  public void scheduleDelivery(
      ShippingProto.DeliveryRequest request,
      StreamObserver<ShippingProto.DeliveryResponse> responseObserver) {
    log.info("Received scheduleDelivery request: {}", request);
    String deliveryDate =
        request.getShippingMethod().equalsIgnoreCase("express") ? "Tomorrow" : "In 5 days";
    DeliverySchedule schedule = new DeliverySchedule(request.getOrderId(), deliveryDate);
    log.info("Scheduled delivery: {}", schedule);

    deliveriesManager.saveDeliverySchedule(request.getOrderId(), schedule);

    ShippingProto.DeliveryResponse response =
        ShippingProto.DeliveryResponse.newBuilder()
            .setSuccess(true)
            .setDeliveryDate(deliveryDate)
            .build();
    responseObserver.onNext(response);
    responseObserver.onCompleted();
    log.info("Sent scheduleDelivery response: {}", response);
  }

  @Override
  public void trackShipment(
      ShippingProto.TrackShipmentRequest request,
      StreamObserver<ShippingProto.TrackShipmentResponse> responseObserver) {
    log.info("Received trackShipment request: {}", request);
    if (!trackingInfoManager.trackingIdExists(request.getTrackingId())) {
      log.warn("Tracking ID not found: {}", request.getTrackingId());
      responseObserver.onNext(
          ShippingProto.TrackShipmentResponse.newBuilder()
              .setSuccess(false)
              .setStatus("Tracking ID not found")
              .build());
    } else {
      ShipmentTrackingInfo info = trackingInfoManager.getTrackingInfo(request.getTrackingId());
      log.info("Retrieved tracking info: {}", info);
      ShippingProto.TrackShipmentResponse response =
          ShippingProto.TrackShipmentResponse.newBuilder()
              .setSuccess(true)
              .setStatus(info.getStatus())
              .setEstimatedDeliveryDate(info.getEstimatedDeliveryDate())
              .build();
      responseObserver.onNext(response);
    }
    responseObserver.onCompleted();
    log.info("Sent trackShipment response");
  }
}
